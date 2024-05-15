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


    def bfs_search(self):
        start_vertex = self.get_vertex('s')
        visited = []
        parent = {}
        queue = []

        
        queue.append(start_vertex)
        visited.append(start_vertex)

        while queue:
            current_vertex = queue.pop(0)

            for neighbor, edge in self.graph[current_vertex].items():
                if neighbor not in visited and edge.residual > 0:
                    visited.append(neighbor)
                    parent[neighbor] = current_vertex
                    queue.append(neighbor)

        return parent
        


    def delete_vertex(self,vertex):
        neighbours = self.neighbours(vertex)

        for v in neighbours:
            self.delete_edge(vertex,v[0])
        del self.graph[vertex]

    def min_capacity(self,parents):
        end_v_key = self.get_vertex('t')
        
        min_flow = float('Inf')
        curr = end_v_key
       
        
        if end_v_key in parents:
    
            while curr != self.get_vertex_items('s'):
                
                parent_ver = parents[curr]
                edge = self.graph[parent_ver][curr]
                if edge.residual < min_flow:
                    min_flow = edge.residual
                curr = parent_ver    
            return min_flow

        return 0    
        

    def path_augmentation(self,parents,min_capacity):
        curr = self.get_vertex('t')
        while curr != self.get_vertex('s'):
            parent_ver = parents[curr]
            edge = self.graph[parent_ver][curr]

            if edge.isResidual:
                edge.residual -= min_capacity
                edgerev = self.graph[curr][parent_ver]
                edgerev.flow -= min_capacity
                edgerev.residual += min_capacity
                curr = parent_ver
            
            else:
                edge.flow += min_capacity
                edge.residual -= min_capacity
                edgerev = self.graph[curr][parent_ver]
                edgerev.residual += min_capacity
                curr = parent_ver
        
        


    def ford_fulkerson_algorithm(self):
        parents = self.bfs_search()

        if self.get_vertex('t') not in parents:
            raise ValueError('Path from s to t not found')
        
        min_capacity = self.min_capacity(parents)
        flow = min_capacity
        while min_capacity > 0:
            self.path_augmentation(parents,min_capacity)

            parents = self.bfs_search()

            min_capacity = self.min_capacity(parents)

            flow += min_capacity
        
        return flow
        
        
    def delete_edge(self,vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            del self.graph[vertex1][vertex2]
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            del self.graph[vertex2][vertex1]

    def neighbours(self,vertex_id):
        try:
            return list(self.graph[vertex_id[0]].items())
        except TypeError:
            return list(self.graph[vertex_id].items())
    
    def vertices(self):
        return list(self.graph.keys())
    
    def get_vertex(self,vertex_id):
        for vert, k in self.graph.items():
            if vert == vertex_id:
                return vert
        
    def get_vertex_items(self,vertex_id):
        for vert, k in self.graph.items():
            if vert == vertex_id:
                return vert.key
        
    
    
    def get_vertexidx(self,vertex):
        return self.graph[vertex]

    def printGraph(self):
        print("------GRAPH------")
        vertic = self.vertices()
        for v in vertic:
            print(v, end = " -> ")
            for (n, w) in self.neighbours(v):
                print(n, w, end=";")
            print()
        print("-------------------")       

        
def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graphs = [graf_0,graf_1,graf_2]

    for graf in graphs:

        graph = ListGraph()

        for data in graf:
            vert1 = Vertex(data[0])
            vert2 = Vertex(data[1])
            edg = Edge(data[2],False)
            edgRes = Edge(data[2],True)

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
                graph.insert_edge(ex_v2,ex_v1,edgRes)

        graph.printGraph()
        
        print(graph.ford_fulkerson_algorithm())

        graph.printGraph()




main()    