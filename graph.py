# Drew Regan
# Rhodes
# CSC 2065

# Represent the social network as a graph

import json
import networkx as nx
import matplotlib.pyplot as plt

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

# Display graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G) # Use layout for better visual spacing
nx.draw(G,pos,with_labels=False,node_size=20,edge_color="gray",node_color="purple",alpha=0.7)
plt.title("Social Network Graph")
plt.show()
