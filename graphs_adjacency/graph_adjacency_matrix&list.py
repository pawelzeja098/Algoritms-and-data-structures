
import polska
import turtle
class Vertex:
    def __init__(self,key) -> None:
        self.key = key
        # self.data = data

    #compare
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
        
    def is_empty(self):
        if self.graph:
            return False
        return True

    def insert_vertex(self,vertex):
        for i in self.graph:
            if vertex == i:
                return i
        self.graph[vertex] = {}
        return None

    def insert_edge(self,vertex1, vertex2, edge = None):
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



class MatrixGraph():
    def __init__(self, value = 0) -> None:
        self.adjmatrix = []
        self.value = value
        self.neighbours_list = []
        

    def is_empty(self):
        if self.adjmatrix:
            return False
        return True

    def insert_vertex(self,vertex):
        
        if vertex not in self.adjmatrix:
            self.adjmatrix.append(vertex)
            for row in self.neighbours_list:
                row.append(0)
            self.neighbours_list.append([0] * len(self.adjmatrix))
            return vertex
        return None

    
    def insert_edge(self,vertex1, vertex2, edge = 1):
        idx1 = self.adjmatrix.index(vertex1)
        idx2 = self.adjmatrix.index(vertex2)
        self.neighbours_list[idx1][idx2] = edge
        self.neighbours_list[idx2][idx1] = edge
    
    def delete_vertex(self,vertex):
        idx = self.adjmatrix.index(vertex)
        del self.adjmatrix[idx]
        del self.neighbours_list[idx]
        for row in self.neighbours_list:
            del row[idx]

    
    def delete_edge(self,vertex1, vertex2):
        idx1 = self.adjmatrix.index(vertex1)
        idx2 = self.adjmatrix.index(vertex2)
        self.neighbours_list[idx1][idx2] = 0
        self.neighbours_list[idx2][idx1] = 0

    def neighbours(self,vertex_id):
        idx = self.adjmatrix.index(vertex_id)
        return [(self.adjmatrix[i], self.neighbours_list[idx][i]) for i in range(len(self.adjmatrix)) if self.neighbours_list[idx][i] != 0]
    
    def vertices(self):
        return self.adjmatrix
    

    def get_vertexIDX(self,vertex_id):
        idx = 0
        for vert in self.adjmatrix:
            idx += 1
            if vert.key == vertex_id:
                return idx
    
    def get_vertex(self,vertex_id):
        for vert in self.adjmatrix:
            if vert.key == vertex_id:
                return vert
        return None

def main(graph):
    data = polska.graf
    graph = graph
    
    for i in data:
        vert1 = Vertex(i[0])
        vert2 = Vertex(i[1])


        ex_v1 = graph.insert_vertex(vert1)
        ex_v2 = graph.insert_vertex(vert2)

        if ex_v1 is None and ex_v2 is None:
            graph.insert_edge(vert1,vert2)

        
        elif ex_v1 is None and ex_v2 is not None:
            graph.insert_edge(vert1,ex_v2)
        
        elif ex_v2 is None and ex_v1 is not None:
            graph.insert_edge(ex_v1,vert2)
        
        else:
            graph.insert_edge(ex_v1,ex_v2)
    graph.delete_vertex(graph.get_vertex('K'))
    graph.delete_edge(graph.get_vertex('W'),graph.get_vertex('E'))
    polska.draw_map(graph)

graphL = ListGraph()
graphM = MatrixGraph()

# main(graphL)
main(graphM)
