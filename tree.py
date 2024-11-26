# 11/25/2024
# Daniel Bradford
# Front Range Community College

import json
import networkx as nx
import matplotlib.pyplot as plt

n_start = 4
n_end = 100
id = str(n_start)

# Load the data
with open('SocialNetworkData_10K.json', 'r') as f: 
    data = json.load(f)

# Create a NetworkX graph
G = nx.Graph()

# Add nodes and edges
for user_id, user_data in data.items():
    G.add_node(user_id, **user_data)
    for connection in user_data['connections']:
        # Use age gap as edge weight
        G.add_edge(user_id, str(connection), w=abs(user_data['age'] - data[str(connection)]['age']))

# Find minimum spanning tree/forest using age gap between connecitons as the weight
tree = nx.minimum_spanning_tree(nx.subgraph(G, list(G.nodes())[n_start:n_end]), weight='w')

# Discard disconnected components from tree containing n_start
connected_tree = tree.subgraph(nx.node_connected_component(tree, id))

# Print results and display in bfs layout
print(list(tree.edges()))  
nx.draw(connected_tree, pos=nx.bfs_layout(connected_tree, id))

# Label edges with age gap bewteen connections
nx.draw_networkx_edge_labels(connected_tree, pos=nx.bfs_layout(connected_tree, id))
plt.show()