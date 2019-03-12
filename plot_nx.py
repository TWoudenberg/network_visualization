### Plot network figure using networkx package

### Importing packages
# Hack to fix matplotlib
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")


# Hack to fix missing PROJ4 env var
import os
import conda
conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

# Regular packages
import matplotlib.pyplot as plt
import networkx as nx


def plot_nx(graph, directory, figure_name, figure_x=9, figure_y=10, figure_format="png", resolution=300):
    plt.figure(figsize=(figure_x, figure_y))
    nx.draw_networkx(graph)

    figure_file = os.path.join(directory, figure_name)
    plt.savefig(figure_file, format=figure_format, dpi=resolution)
    plt.show()
