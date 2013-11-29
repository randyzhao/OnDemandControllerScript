'''
Created on Nov 27, 2013

@author: randyzhao
'''
import sys

class InternetTopology:
    '''
    This class is used to store the information of Internet Topology graph
    just like Internet Topology Zoo project
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.nodes = {}
        self.edges = []
        
    def add_node(self, nid, longitude, latitude, node_type):
        '''
        Add a node with given node id, longitude, latitude and node type 
        The type of node can be helpful to plot it out
        '''
        self.nodes[nid] = (nid, longitude, latitude, node_type)
    
    def add_edgs(self, source_node_id, dest_node_id, label, edge_type):
        self.edges.add((source_node_id, dest_node_id, label, edge_type))
        
    def set_size(self, height, width):
        self.height = height
        self.width = width
    
def unmarshell_from_file(file_path):
    it = InternetTopology()
    it.height, it.width = [int(x) for x in sys.stdin.readline()]
    node_count = int(sys.stdin.readline())
    for _ in range(node_count):
        nid, log, lat, node_type = [x for x in sys.stdin.readline()]
        it.add_node(int(nid), int(log), int(lat), node_type)
    edge_count = int(sys.stdin.readline())
    for _ in range(edge_count):
        sni, dni, lab, et = [x for x in sys.stdin.readline()]
        it.add_edgs(int(sni), int(dni), lab, et)
    return it



    
        