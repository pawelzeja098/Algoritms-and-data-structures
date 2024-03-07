class Matrix:
    def __init__(self,A,value = 0) -> None:
        if isinstance(A, tuple):
            A = [[value for i in range(A[1])] for j in range(A[0])]
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
        
    
    
    def __mul__(self, other: 'Matrix') -> 'Matrix':
        x = self.size()[1]
        y = other.size()[0]
        if self.size()[1] != other.size()[0]:
            raise ValueError("Incompatible shapes")
    
        C = [[0 for i in range(self.size()[0])] for j in range(other.size()[1])]

        for i in range(len(self.A)):
            for j in range(len(other.A[0])):
                for k in range(len(other.A)):
                    C[i][j] += (self.A[i][k] * other.A[k][j])
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
    


def transpose(matrix):
    C = Matrix((matrix.size()[1], matrix.size()[0]))
    m, n = matrix.size()
    for i in range(m):
        for j in range(n):
            C[j][i] = matrix[i][j]
    return C
        

m1 = Matrix([[1,0,2],[-1,3,1]])
m2 = Matrix((2,3),value = 1)
m3 = Matrix([[3,1],[2,1],[1,0]])


print(f"Transpozycja macierzy m1: \n{transpose(m1)}")

print(f"Suma macierzy m1 i m2: \n{m1+m2}")

print(f"Wynik mnożenia macierzy m1 i m3: \n{m1*m3}")
