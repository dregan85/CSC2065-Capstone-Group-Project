import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the data
with open('SocialNetworkData_10K.json', 'r') as f: 
    data = json.load(f)

# Create a NetworkX graph
G = nx.Graph()

# Add nodes and edges
for user_id, user_data in data.items():
    G.add_node(user_id, **user_data)
    for connection in user_data['connections']:
        G.add_edge(user_id, str(connection))

# Basic network analysis
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Average degree: {sum(dict(G.degree()).values()) /
G.number_of_nodes():.2f}")

# Visualize a small subset of the network
subgraph = nx.subgraph(G, list(G.nodes())[:100])
pos = nx.spring_layout(subgraph)
nx.draw(subgraph, pos, with_labels=False, node_size=30)
plt.title("Subset of Social Network")
plt.show()

# Example of more advanced analysis (community detection)
from networkx.algorithms import community

communities = community.greedy_modularity_communities(G)
print(f"Number of communities detected: {len(communities)}")