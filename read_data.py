# Read network and schedule data from .xlsx input file

import pandas as pd


def read_data(input_file):
    input_file = 'network_input.xlsx'
    airports = pd.read_excel(input_file, sheetname=0,)
    airports.head()
    routes = pd.read_excel(input_file, sheetname=1, )
    routes.head()

    return airports, routes
