#inf  o krawędzi none
#mozna liniowo wyszukiwac numer
import polska
import turtle
class Vertex():
    def __init__(self,key,data) -> None:
        self.key = key
        self.data = data

    #compare
    def __eq__(self, value: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass
    
class ListGraph():
    def __init__(self) -> None:
        self.graph = {}
        
    def is_empty(self):
        pass

    def insert_vertex(self,vertex):
        self.graph[vertex] = {}

    def insert_edge(self,vertex1, vertex2, egde):
        self.graph[vertex1] = egde

    def delete_vertex(self,vertex):
        pass

    
    def delete_edge(self,vertex1, vertex2):
        pass



class MatrixGraph():
    def __init__(self) -> None:
        pass
    
    def is_empty(self):
        pass

    def insert_vertex(self,vertex):
        pass
    

    def insert_edge(self,vertex1, vertex2, egde):
        pass

    def delete_vertex(self,vertex):
        pass

    
    def delete_edge(self,vertex1, vertex2):
        pass


def main():
    pass

def test():
    graph = ListGraph()
