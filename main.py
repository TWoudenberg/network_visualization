### create network visualization

### Import packages
# regular packages and modules
import os.path
import networkx as nx
from read_data import read_data
from plot_nx import plot_nx
from plot_bm import plot_bm

### Script
# Specify input file and directory
directory = os.path.dirname(__file__)
filename = 'network_input.xlsx'

# Read network data
# Airports: 0: IATA code, 1: latitude, 2: longitude
# Routes: 0: origin, 1: destination, 2: frequency
(airports, routes) = read_data(filename)

# read dataframe headers
header_airports = list(airports)
header_routes = list(routes)

# Generate graph network
graph = nx.from_pandas_edgelist(routes, source=header_routes[0], target=header_routes[1], edge_attr=header_routes[2], create_using=nx.DiGraph())

# Plotting figure style 1
# figure_name = "figures/map_nx.png"
# plot_nx(graph,directory,figure_name)

# Plotting figure style 2
figure_name = "figures/map_bm.png"
plot_bm(graph, airports, routes, header_airports, header_routes, directory, figure_name)
