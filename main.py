# create network visualization

import os.path
import pandas as pd

from read_data import read_data

# specify input file
directory = os.path.dirname(__file__)
filename = 'network_input.xlsx'
inputFile = os.path.join(directory, filename)

# read network data
(airports, routes) = read_data(inputFile)

a=1