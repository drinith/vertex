from itertools import chain, combinations
import networkx as nx

class vertex:

    def powerset(self,iterable):
        """Return the powerset of an iterable as a list of lists.
        
        Args:
            iterable (list): list of elements to take the powerset of
            
        Example:
            >>> for x in powerset([1, 2, 3]):
            >>>    print(x)
            ()
            (1,)
            (2,)
            (3,)
            (1, 2)
            (1, 3)
            (2, 3)
            (1, 2, 3)

        Returns:
            iterator: iterator over the powerset of the input list
        """
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    def subsets(self,iterable, lenght=None):
        K = lenght or len(iterable)
        for x in self.powerset(iterable):
            if len(x) > K:
                break
            yield x

    def is_vertex_cover_brute_force(self,edges, subset_nodes):

       for u, v in edges:
        if u not in subset_nodes and v not in subset_nodes:
            return False
        return True


if __name__=='__main__':

    n = 5  # number of vertices
    m = 1  # number of edges for each new vertex in barabasi_albert_graph

    graph = nx.barabasi_albert_graph(n, m, seed=42)
    nx.draw_circular(graph, with_labels=True)