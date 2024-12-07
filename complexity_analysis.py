# Drew Regan
# Rhodes
# CSC 2065


import json
import networkx as nx
import matplotlib.pyplot as plt
import time

# Load data
with open('SocialNetworkData_10K.json', 'r') as f:
    data = json.load(f)

# Create graph
G = nx.Graph()

# Add nodes and edges
# Each user ID becomes a node, and each connection becomes an edge
for user_id, user_data in data.items():
    G.add_node(user_id, **user_data)
    for connection in user_data['connections']:
        G.add_edge(user_id, str(connection))

# Function to measure execution time
def measure_time(func, *args, **kwargs):
    start_time = time.perf_counter() # Record start time
    func(*args, **kwargs) # Perform the function
    end_time = time.perf_counter() # Record end time
    return end_time - start_time # return time measurement

# Function to perform time complexity analysis
# Big O notations used for each operation:
# Add Node O(1) - takes constant time because it only adds a single entry
# Remove Node O(1) - takes constant time because it only removes a single entry
# Add Edge O(1) - takes constant time because it only adds a single entry
# Remove Edge O(1) - takes constant time because it only removes a single entry
# Check Neighbors O(d) - takes time depending on how many neighbors each node has (degree)
# Breadth First Search O(V + E) - time taken is proportional to to the total number of nodes + edges
# Depth First Search O(V + E) - time taken is proportional to to the total number of nodes + edges
# Adjacency Matrix O(V^2) - time taken is proportional to the square number of nodes

def complexity_analysis(graph):
    results = {}

    # Add a node to the graph
    results['Add Node'] = measure_time(graph.add_node, 'temp_node')

    # Remove a node from the graph
    results['Remove Node'] = measure_time(graph.remove_node, 'temp_node')

    # Add edge between nodes
    results['Add Edge'] = measure_time(graph.add_edge, 'node1', 'node2')

    # Remove edge between nodes
    if graph.has_edge('node1', 'node2'):
        results['Remove Edge'] = measure_time(graph.remove_edge, 'node1', 'node2')
    else:
        results['Remove Edge'] = None

    # Check node neighbors
    if graph.number_of_nodes() > 0:
        first_node = next(iter(graph.nodes)) # Pick a node
        results['Check Neighbors'] = measure_time(graph.neighbors, first_node)

    # Breadth First Search
    if graph.number_of_nodes() > 0:
        first_node = next(iter(graph.nodes)) # Pick a node
        results['Breadth First Search'] = measure_time(nx.bfs_edges, graph, source=first_node)

    # Depth First Search
    if graph.number_of_nodes() > 0:
        first_node = next(iter(graph.nodes)) # Pick a node
        results['Depth First Search'] = measure_time(nx.dfs_edges, graph, source=first_node) 

    # Adjacency matrix
    results['Adjacency Matrix'] = measure_time(nx.adjacency_matrix, graph)

    return results

# Perform time complexity analysis on the graph
results = complexity_analysis(G)

# Print results of time complexity analysis
print ("Time Complexity Analysis:")
for operation, time_taken in results.items():
    if time_taken is not None:
        print(f"{operation}: {time_taken:.6f}") # Print taken time in seconds
    else:
        print(f"{operation}: N/A")

# Display graph
operations = list(results.keys())
times = [time if time is not None else 0 for time in results.values()]

plt.figure(figsize=(8, 5))
bars = plt.barh(operations, times, color='orange', alpha=0.8) # Create bar chart
plt.xscale('log') # Use a logarithmic scale for the x-axis to make the smaller operation times visible
plt.xlabel("Time (log(seconds))") # X axis label
plt.title("Time Complexity Analysis (Log Scale)") # Add chart title

# Add time in seconds to each bar for reference
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.6f}s', va='center', ha='left', color='blue')

# Display graph
plt.show()
