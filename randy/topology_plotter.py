'''
Created on Nov 29, 2013

@author: randyzhao
'''
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import internetTopology as itopo

def plot_topology(topo):
    G = nx.Graph()
    #add nodes
    for nid, longitude, latitude, node_type in topo.nodes.values():
        G.add_node(nid, pos=(longitude, latitude), node_type=node_type)
    #add edges
    for source_node_id, dest_node_id, label, edge_type in topo.edges:
        G.add_edge(source_node_id, dest_node_id, label=label, edge_type=edge_type)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos)
    plt.show()

it = itopo.unmarshell_from_file('topo.txt')
plot_topology(it)
        