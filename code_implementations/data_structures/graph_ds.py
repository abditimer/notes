# Graphs
# ------
# Graphs have vertices and edges. They are represented either as:
#   1. Adjancency Matrix
#       - size of VxV: If M[i][j]=1, then there is an edge between vertex i and j
#       - Pos: remove an edge is O(1), search is O(1)
#       - Neg: large space used O(n²)
#   2. Adjancency List
#       - Array of lists: size of array is number of vertices. array[i] = list of vertices adjacent to ith vertex
#       - pos: space saved in memory O(V+E)
#       - neg: queries to search if there is an edge from V1 to V2 not efficient -> O(V)
# -------

class GraphAM:
    # This represents a Graph implemented as an Adjacent Matrix
    def __init__(self, numvertex):
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {} # dictionary with vertex_id=vertex_representation
        self.verticeslist = [0]*numvertex # instantiate empty list of all vertices

    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id
    
    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        # if graph is directed - dont add below
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist
    
    def get_edges(self):
        edges=[]
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adjMatrix[i][j] != -1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges
    
    def get_matrix(self):
        return self.adjMatrix
    
# time to test
def build_adjancy_matrix():
    # instantiate our graph
    graph = GraphAM(6)
    # add our vertices
    graph.set_vertex(0, 'a')
    graph.set_vertex(1, 'b')
    graph.set_vertex(2, 'c')
    graph.set_vertex(3, 'd')
    graph.set_vertex(4, 'e')
    graph.set_vertex(5, 'f')
    # add our edges
    graph.set_edge('a', 'e', 10)
    graph.set_edge('a', 'c', 20)
    graph.set_edge('c', 'b', 30)
    graph.set_edge('b', 'e', 40)
    graph.set_edge('e', 'd', 50)
    graph.set_edge('f', 'e', 60)
    
    print('Vertices of Graph:')
    print(graph.get_vertex())
    print('Edges of Graph:')
    print(graph.get_edges())
    print('Adjancy Matrix')
    print(graph.get_matrix())

class AdjNode:
    # represents adjancy list of the node
    def __init__(self, data):
        self.vertex = data
        self.next = None

class GraphAL:
    # Implements an Adjacent List Graph
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    
    def add_edge(self, frm, to):
        # function to add an edge in an undirected graph
        node = AdjNode(to)
        node.next = self.graph[frm]
        self.graph[frm] = node

        node = AdjNode(frm)
        node.next = self.graph[to]
        self.graph[to] = node
    
    def print_graph(self):
        for i in range(self.V):
            print('Adjacency list of vertex {}\n head'.format(i), end='')
            temp = self.graph[i]
            while temp:
                print(' -> {}'.format(temp.vertex), end="")
                temp = temp.next 
            print(' \n')

def build_adjacency_list():
    graph = GraphAL(5)
    graph.add_edge(0,1)
    graph.add_edge(0,4)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.print_graph()

def main():
    #build_adjancy_matrix()
    build_adjacency_list()


if __name__ == "__main__":
    main()

