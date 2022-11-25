from itertools import chain, combinations
import networkx as nx

class Vertex:

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

    #https://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm-2/
    # The function to print vertex cover
    def printVertexCover(self):
         
        # Initialize all vertices as not visited.
        visited = [False] * (self.V)
         
        # Consider all edges one by one
        for u in range(self.V):
             
            # An edge is only picked when
            # both visited[u] and visited[v]
            # are false
            if not visited[u]:
                 
                # Go through all adjacents of u and
                # pick the first not yet visited
                # vertex (We are basically picking
                # an edge (u, v) from remaining edges.
                for v in self.graph[u]:
                    if not visited[v]:
                         
                        # Add the vertices (u, v) to the
                        # result set. We make the vertex
                        # u and v visited so that all
                        # edges from/to them would
                        # be ignored
                        visited[v] = True
                        visited[u] = True
                        break
 
        # Print the vertex cover
        for j in range(self.V):
            if visited[j]:
                print(j, end = ' ')
                 
        print()


if __name__=='__main__':

    n = 5  # number of vertices
    m = 3  # number of edges for each new vertex in barabasi_albert_graph

    graph = nx.barabasi_albert_graph(n, m, seed=42)
    nx.draw_circular(graph, with_labels=True)

    nodes = list(graph.nodes)
    edges = list(graph.edges)

    v = Vertex()

    print(f'nodes: {nodes}\nedges: {edges}')

    for subset in v.subsets(nodes):
        print(subset)

    K = 2
for subset in v.subsets(nodes, K):
    print(subset)


K = 3
for subset in v.subsets(nodes, K):
    print(f'subset tested: {subset}')
    if v.is_vertex_cover_brute_force(edges, subset):
        print(f'Subset {subset} is a vertex cover')
        break