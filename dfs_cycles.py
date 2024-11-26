# 11/25/2024
# Daniel Bradford
# Front Range Community College

import json
import networkx as nx
import matplotlib.pyplot as plt

n_start = 700
n_end = 1200

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

# Uses depth-first search to find a cycle in subgraph from node n_start to n_end
try:
    print(list(nx.find_cycle(nx.subgraph(G, list(G.nodes())[n_start:n_end]))))
except nx.NetworkXNoCycle:
    print('No cycle found starting from node', n_start, 'to node', n_end)