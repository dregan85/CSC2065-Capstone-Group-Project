# 9/24/2024
# Daniel Bradford
# Front Range Community College
import json
import networkx as nx
import matplotlib.pyplot as plt

n_start = 1000
n_end = 1400

# Load data
with open('SocialNetworkData_10K.json', 'r') as f: 
    data = json.load(f)

# Create graph
G = nx.Graph()

# Add nodes and edges
for user_id, user_data in data.items():
    G.add_node(user_id, **user_data)
    for connection in user_data['connections']:
        G.add_edge(user_id, str(connection))

# Show adjacency matrix
plt.imshow(nx.adjacency_matrix(G, list(G.nodes())[n_start:n_end]).toarray(), cmap='binary')
plt.show()