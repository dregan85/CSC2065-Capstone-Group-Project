import json
import networkx as nx
from collections import deque

# Load JSON data
with open('SocialNetworkData_10K.json', 'r') as f:
        graph = json.load(f)

# Create graph
G = nx.Graph()

# Add nodes and edges
for user_id, user_data in graph.items():
    G.add_node(user_id, **user_data)
    for connection in user_data['connections']:
        G.add_edge(user_id, str(connection))
    
def bfs_shortest_path (graph, start):
    # Get the shortest path
    shortest_paths = {start: [start]}

    # Queue for BFS traversal
    queue = deque([start])


    while queue:
        current_node = queue.popleft()

        if current_node in graph:
            for neighbor in graph[current_node]['connections']:
                 neighbor = str(neighbor)
            # If neighbor hasn't been visisted yet
            if neighbor not in shortest_paths:
                # Append current node's path to neighbor
                queue.append(neighbor)
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return shortest_paths

# hardcoded since I wasn't given any start node and no input by a user was requested
start_node = '120'
shortest_paths = bfs_shortest_path(graph, start_node)

print(f'Shortest paths from starting node {start_node}:')
for node, path in shortest_paths.items():
    print(f'Shortest path {node}: {path}')

print(shortest_paths)

