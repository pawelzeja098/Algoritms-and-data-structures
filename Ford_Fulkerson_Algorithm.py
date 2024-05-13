class Vertex:
    def __init__(self,key) -> None:
        self.key = key
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex):
            return self.key == other.key
        else:
            return self.key == other

    def __hash__(self) -> int:
        return hash(self.key)

    def __str__(self) -> str:
        return f'{self.key}'

class Edge:
    def __init__(self,capacity,isResidual) -> None:
        self.capacity = capacity
        self.isResidual = isResidual
        if self.isResidual:
            self.flow = 0
            self.residual = 0
        self.flow = 0
        self.residual = capacity

    def __repr__(self) -> str:
        return f'{self.flow} {self.residual} {self.isResidual}'
    


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
        # self.graph[vertex2][vertex1] = edge



    def Bfs_search(self):
        visited = []
        parent = {}
        queue = []
        
        visited.append(self.get_vertex('s'))
        queue.append(self.get_vertex('s'))

        while queue:
            curr = queue[0]
            neighbs = self.neighbours(curr)
            for ver in neighbs:
                if ver not in visited and ver[1].flow > 0 :
                    visited.append(ver)
                    parent[curr] = ver
                    #TO DO: DODANIE DO SŁOWNIKA PARENT
                    queue.append(ver)
        return parent

    def delete_vertex(self,vertex):
        neighbours = self.neighbours(vertex)

        for v in neighbours:
            self.delete_edge(vertex,v[0])
        del self.graph[vertex]

    def min_capacity(self,parents):
        end_v = self.get_vertex('t')
        min_flow = float('Inf')
        curr = end_v
        if parents[end_v]:
            while curr != self.get_vertex('s'):
                for p in parents[curr]:
                    if p.flow < min_flow:
                        min_flow = p.flow


        return 0    
        







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
            

        
def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]

    graph = ListGraph()

    for data in graf_0:
        vert1 = Vertex(data[0])
        vert2 = Vertex(data[1])
        edg = Edge(data[3],False)
        edgRes = Edge(data[3],True)

        ex_v1 = graph.insert_vertex(vert1)
        ex_v2 = graph.insert_vertex(vert2)

        if ex_v1 is None and ex_v2 is None:
            graph.insert_edge(vert1,vert2,edg)
            graph.insert_edge(vert2,vert1,edgRes)

        
        elif ex_v1 is None and ex_v2 is not None:
            graph.insert_edge(vert1,ex_v2,edg)
            graph.insert_edge(ex_v2,vert1,edgRes)
        
        elif ex_v2 is None and ex_v1 is not None:
            graph.insert_edge(ex_v1,vert2,edg)
            graph.insert_edge(vert2,ex_v1,edgRes)
        
        else:
            graph.insert_edge(ex_v1,ex_v2,edg)
            graph.insert_edge(ex_v1,ex_v2,edgRes)




main()    