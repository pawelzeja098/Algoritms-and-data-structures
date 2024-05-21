class Vertex:
    def __init__(self,key) -> None:
        self.key = key
        self.colour = None

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex):
            return self.key == other.key
        else:
            return self.key == other

    def __hash__(self) -> int:
        return hash(self.key)

    def __str__(self) -> str:
        return f'{self.key}'

class ListGraph:
    def __init__(self) -> None:
        self.graph = {}
        self.intree = {}
        self.distance = {}
        self.parent = {}
        
    def is_empty(self):
        if self.graph:
            return False
        return True

    def insert_vertex(self,vertex):
        for i in self.graph:
            if vertex == i:
                return i
        self.graph[vertex] = {}
        self.intree[vertex] = 0
        self.distance[vertex] = float('Inf')
        self.parent[vertex] = None
        return None

    def insert_edge(self,vertex1, vertex2, edge):
        self.graph[vertex1][vertex2] = edge
        self.graph[vertex2][vertex1] = edge
        

    def delete_vertex(self,vertex):
        neighbours = self.neighbours(vertex)

        for v in neighbours:
            self.delete_edge(vertex,v[0])
        del self.graph[vertex]

    
    def delete_edge(self,vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            del self.graph[vertex1][vertex2]
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            del self.graph[vertex2][vertex1]

    def neighbours(self,vertex_id):
        return list(self.graph[vertex_id].items())
    
    def vertices(self):
        return list(self.graph.keys())
    
    def get_vertex(self,vertex_id):
        for vert in self.graph:
            if vert == vertex_id:
                return vert

    def printGraph(g):
        print("------GRAPH------")
        for v in g.vertices():
            print(v, end = " -> ")
            for (n, w) in g.neighbours(v):
                print(n, w, end=";")
            print()
        print("-------------------")


class MST:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.MST = ListGraph()

    def prim(self):
        start_vertex = next(iter(self.graph.vertices()))
        self.graph.distance[start_vertex] = 0
        while not all(self.graph.intree.values()):
            current_vertex = min(
                (v for v in self.graph.vertices() if self.graph.intree[v] == 0),
                key=lambda v: self.graph.distance[v])

            self.graph.intree[current_vertex] = 1

            if self.graph.parent[current_vertex] is not None:
                parent_vertex = self.graph.parent[current_vertex]
                edge_weight = self.graph.graph[current_vertex][parent_vertex]
                self.MST.insert_vertex(current_vertex)
                self.MST.insert_vertex(parent_vertex)
                self.MST.insert_edge(current_vertex, parent_vertex, edge_weight)

            for neighbour, weight in self.graph.neighbours(current_vertex):
                if self.graph.intree[neighbour] == 0 and weight < self.graph.distance[neighbour]:
                    self.graph.distance[neighbour] = weight
                    self.graph.parent[neighbour] = current_vertex

        return self.MST





def main():
    data = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
    graph = ListGraph()
    


    
    
    for i in data:
        vert1 = Vertex(i[0])
        vert2 = Vertex(i[1])
        edge = i[2]


        ex_v1 = graph.insert_vertex(vert1)
        ex_v2 = graph.insert_vertex(vert2)

        if ex_v1 is None and ex_v2 is None:
            graph.insert_edge(vert1,vert2,edge)

        
        elif ex_v1 is None and ex_v2 is not None:
            graph.insert_edge(vert1,ex_v2,edge)
        
        elif ex_v2 is None and ex_v1 is not None:
            graph.insert_edge(ex_v1,vert2,edge)
        
        else:
            graph.insert_edge(ex_v1,ex_v2,edge)

    mst_inst = MST(graph)
    mst_res = mst_inst.prim()

    mst_res.printGraph()
    
main()