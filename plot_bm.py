### Plot network figure using basemap package

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
from mpl_toolkits.basemap import Basemap as bm


def plot_bm(graph, nodes, edges, directory, figure_name, figure_x=9, figure_y=10, figure_format="png", resolution=300):

    # read dataframe headers
    header_nodes = list(nodes)
    header_edges = list(edges)

    # setup Basemap style
    plt.figure(figsize=(figure_x, figure_y))
    m = bm(
        projection='merc',
        llcrnrlon=125,
        llcrnrlat=25,
        urcrnrlon=145,
                urcrnrlat=45,
        lat_ts=0,
        resolution='l',
        suppress_ticks=True
    )

    # prepare position data
    offset = 100000
    mx, my = m(nodes[header_nodes[2]].values, nodes[header_nodes[1]].values)
    pos = {}
    pos_label = {}
    for count, elem in enumerate(nodes[header_nodes[0]]):
        pos[elem] = (mx[count], my[count])
        pos_label[elem] = (mx[count] + offset, my[count] + offset)

    # prepare node and edge attributes
    width = [graph[i][j][header_edges[2]] for i, j in graph.edges]
    edge_labels = nx.get_edge_attributes(graph, header_edges[3])



    # add attributes to network
    nx.draw_networkx_nodes(
        G=graph,
        pos=pos,
        node_list=graph.nodes(),
        node_color='r',
        alpha=1,
        node_size=100
    )
    nx.draw_networkx_edges(
        G=graph,
        pos=pos,
        edges=edges,
        edge_color='g',
        width=width,
        alpha=1,
        arrows=False
    )
    nx.draw_networkx_labels(
        G=graph,
        pos=pos_label,
        label=nodes[header_nodes[0]],
        font_size=16,
        font_color='k'
    )
    nx.draw_networkx_edge_labels(
        G=graph,
        pos=pos,
        edge_labels=edge_labels
    )

    # draw map details
    m.drawcountries(linewidth=1)
    m.drawstates(linewidth=0.2)
    m.drawcoastlines(linewidth=1)
    plt.tight_layout()

    # output figure
    figure_file = os.path.join(directory, figure_name)
    plt.savefig(figure_file, format=figure_format, dpi=resolution)
    plt.show()
