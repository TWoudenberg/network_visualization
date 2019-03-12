### create network visualization

# import packages
import networkx as nx
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap as bm

from read_data import read_data

# specify input file
filename = 'network_input.xlsx'

# read network data
(airports, routes) = read_data(filename)

# generate graph network
graph = nx.from_pandas_edgelist(routes, source='origin', target='destination', edge_attr='frequency',create_using=nx.DiGraph())
a=1