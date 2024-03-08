# Import necessary modules from COMPAS
from compas.data import DataManager
from compas.analysis import Network

# Create a data manager instance
data_manager = DataManager()

# Load sample data (e.g., network data)
data_manager.load('network')
network_data = data_manager['network']

# Create a network instance from the loaded data
network = Network.from_data(network_data)

# Perform analysis (e.g., compute shortest path)
source_node = 'A'
target_node = 'B'
shortest_path = network.shortest_path(source_node, target_node)

# Print the shortest path
print("Shortest path from node {} to node {}: {}".format(source_node, target_node, shortest_path))