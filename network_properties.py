# 12/1/2024
# Daniel Bradford
# Front Range Community College

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

# Make sure graph consists of one single connected component
if(nx.is_connected(G)):
    print("Network is connected")
    # Find minimum node degree
    # G.degree returns DegreeView, which needs to be cast to dict for easy value access
    minDegree = min(dict(G.degree()).values())
    print("Minimum vertex degree =", minDegree)
    # Find upper bound for graoh connectivity
    print("Vertex and edge connectivity <=", minDegree)
    # Check if graph is planar
    if nx.is_planar(G):
        print("Network is planar")
    else:
        print("Network is not planar")
else:
    print("Network is disconnected")