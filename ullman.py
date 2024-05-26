from copy import deepcopy
class Matrix:
    def __init__(self,A,value = 0) -> None:
        if isinstance(A, tuple):
            A = [[0 for i in range(A[1])] for j in range(A[0])]
            
        self.A = A
        
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        
        C = []
        if self.size() != other.size():
            raise ValueError("Incompatible shapes")
        for i in range(self.size()[0]):
            row = []
            for j in range(self.size()[1]):
                row.append((self.A[i][j] + other.A[i][j]))
            C.append(row)
        return Matrix(C)
        
    
    
    def __mul__(self, other) -> 'Matrix':

        if isinstance(other,MatrixGraph):
            return self.multiplyMxMG(other)
        elif isinstance(other, Matrix):
            return self.multiplyMxM(other)
        else:
            raise TypeError("Incompatible type")
    
    def multiplyMxMG(self,other: 'MatrixGraph'):
        
        x, n = self.size()
        m, y = other.size()

        if n != m:
            raise ValueError("Incompatible shapes")

        C = [[0 for i in range(y)] for j in range(x)]

        for i in range(x):
            for j in range(y):
                for k in range(n):
                    C[i][j] += self.A[i][k] * other.neighbours_list[k][j]

        return Matrix(C)
        
    
    def multiplyMxM(self,other:'Matrix'):
        
        x, n = self.size()
        m, y = other.size()

        if n != m:
            raise ValueError("Incompatible shapes for multiplication")

        
        C = [[0 for i in range(y)] for j in range(x)]

        
        for i in range(x):
            for j in range(y):
                for k in range(n):
                    C[i][j] += self.A[i][k] * other.A[k][j]

        return Matrix(C)

    def __getitem__(self, indices) -> int:
        return self.A[indices]

    def __str__(self) -> str:
        
        res = ""
        for row in self.A:
            res += "|" + " ".join(map(str,row)) + "|\n"
        return res

    def size(self) -> tuple:
        m = len(self.A) 
        n = len(self.A[0])
        return(m,n)

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

class MatrixGraph:
    
    
    def __init__(self, value = 0) -> None:
        self.adjmatrix = []
        self.value = value
        self.neighbours_list = []
    
    def __eq__(self, other) -> bool:
            return self.adjmatrix == other

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
    
    def size(self) -> tuple:
        m = len(self.neighbours_list) 
        n = len(self.neighbours_list[0])
        return(m,n)
    
    def sum_neighbours_list_row(self,row_index):
        row = self.neighbours_list[row_index]
        return sum(row)


def transpose(matrix):
    C = Matrix((matrix.size()[1], matrix.size()[0]))
    m, n = matrix.size()
    for i in range(m):
        for j in range(n):
            C[j][i] = matrix[i][j]
    return C

def ullman1(l_collumns, M,graphG ,graphP,ull_call,iso_count,curr_row = 0):
        ull_call += 1
        

        if curr_row == M.size()[0]:
            iso = is_isomorfizm(graphP,graphG,M)
            if iso:
                iso_count += 1
                
            return ull_call, iso_count
        
        for col in range(len(l_collumns)):

            
            if l_collumns[col] == False:
                l_collumns[col] = True
                for i in range(M.size()[1]):
                    M[curr_row][i] = 0

                M[curr_row][col] = 1
                ull_call, iso_count = ullman1(l_collumns,M,graphG,graphP,ull_call,iso_count,curr_row + 1)
                l_collumns[col] = False
        
        return ull_call, iso_count


def ullman2(l_collumns, M,graphG ,graphP,ull_call,iso_count,curr_row = 0):
        ull_call += 1
        

        if curr_row == M.size()[0]:
            iso = is_isomorfizm(graphP,graphG,M)
            if iso:
                iso_count += 1
                
            return ull_call, iso_count
        
        M_copy = deepcopy(M)
        for col in range(len(l_collumns)):

            
            if l_collumns[col] == False and M[curr_row][col] != 0:
                l_collumns[col] = True
                for i in range(M_copy.size()[1]):
                    M_copy[curr_row][i] = 0

                M_copy[curr_row][col] = 1
                ull_call, iso_count = ullman2(l_collumns,M_copy,graphG,graphP,ull_call,iso_count,curr_row + 1)
                l_collumns[col] = False
        
        return ull_call, iso_count

def prune(M,P,G):
    changed = True
    while changed:
        changed = False
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    for x in range(len(P.neighbours_list)):
                        if M[i][x] == 1:
                            has_corresponding = False
                            for y in range(len(G.neighbours_list)):
                                if M[x][y] == 1:
                                    has_corresponding = True
                                    break
                            if not has_corresponding:
                                M[i][j] = 0
                                changed = True
                                break
    return M

def ullman3(l_collumns, M,graphG ,graphP,ull_call,iso_count,curr_row = 0):
        ull_call += 1
        

        if curr_row == M.size()[0]:
            iso = is_isomorfizm(graphP,graphG,M)
            if iso:
                iso_count += 1
                
            return ull_call, iso_count
        
        M_copy = deepcopy(M)

        M_copy = prune(M_copy,graphP,graphG)

        for col in range(len(l_collumns)):

            
            if l_collumns[col] == False and M[curr_row][col] != 0:
                l_collumns[col] = True
                for i in range(M_copy.size()[1]):
                    M_copy[curr_row][i] = 0

                M_copy[curr_row][col] = 1
                ull_call, iso_count = ullman3(l_collumns,M_copy,graphG,graphP,ull_call,iso_count,curr_row + 1)
                l_collumns[col] = False
        
        return ull_call, iso_count

def is_isomorfizm(P,G,M):
    mxg = M*G
    transposed = transpose(mxg)
    res = M*transposed
    

    if P.neighbours_list == res.A:
        return True
    
    return False

def transpose(matrix):
    C = Matrix((matrix.size()[1], matrix.size()[0]))
    m, n = matrix.size()
    for i in range(m):
        for j in range(n):
            C[j][i] = matrix[i][j]
    return C


def main():
    data_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    data_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    data = data_G
    


    graphG = MatrixGraph()
    graphP = MatrixGraph()

    graphs = [graphG, graphP]
    for graph in graphs:
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
        data = data_P

    l = len(graphP.adjmatrix), len(graphG.adjmatrix)
    M = Matrix(l)
    l_columns = [False for i in range(len(M[0]))]

    
    iso_count = 0
    ull_call = 0
    ull_call, iso_count = ullman1(l_columns,M,graphG,graphP,ull_call,iso_count)

    print(iso_count,ull_call)

    M0 = Matrix(l)
    
    for i in range(graphP.size()[0]):

        P_len = graphP.sum_neighbours_list_row(i)
        for j in range(graphG.size()[0]):
            G_len = graphG.sum_neighbours_list_row(j)
            if P_len <= G_len:
                M0[i][j] = 1
    l_columns = [False for i in range(len(M[0]))]
    iso_count = 0
    ull_call = 0
    ull_call, iso_count = ullman2(l_columns,M0,graphG,graphP,ull_call,iso_count)
    
    print(iso_count,ull_call)

    l_columns = [False for i in range(len(M[0]))]
    iso_count = 0
    ull_call = 0
    ull_call, iso_count = ullman3(l_columns,M0,graphG,graphP,ull_call,iso_count)
    
    print(iso_count,ull_call)


main()