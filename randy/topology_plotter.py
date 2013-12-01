'''
Created on Nov 29, 2013

@author: randyzhao
'''
import networkx as nx
import matplotlib.pyplot as plt
import internetTopology as itopo

def plot_topology(topo):
    G = nx.Graph()
    #add nodes
    for nid, longitude, latitude, node_type in topo.nodes.values():
        ncolor = node_type[0]
        node_size = 300
        if len(node_type) != 1:
            node_size = 1000
        G.add_node(nid, pos=(longitude, latitude), node_type='', node_size=node_size, node_color=ncolor)
    #add edges
    for source_node_id, dest_node_id, label, edge_type in topo.edges:
        G.add_edge(source_node_id, dest_node_id, label=label, edge_type=edge_type)
    pos = nx.get_node_attributes(G, 'pos')
    node_size = nx.get_node_attributes(G, 'node_size')
    node_color = nx.get_node_attributes(G, 'node_color')
    nx.draw(G, pos=pos, node_size=node_size.values(), node_color=node_color.values())
    plt.show()

it = itopo.unmarshell_from_file('graph.txt')
plot_topology(it)
        