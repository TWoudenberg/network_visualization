# Read network and schedule data from .xlsx input file

import pandas as pd


def read_data(input_file):

    airports = pd.read_excel(input_file, sheet_name=0)
    airports.head()
    routes = pd.read_excel(input_file, sheet_name=1)
    routes.head()

    return airports, routes
