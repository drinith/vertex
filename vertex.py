from itertools import chain, combinations
import networkx as nx

class vertex:

    def is_vertex_cover_brute_force(edges, subset_nodes):

       for u, v in edges:
        if u not in subset_nodes and v not in subset_nodes:
            return False
        return True