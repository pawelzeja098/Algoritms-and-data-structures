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
    
    
    def delete_row(self, index):
        del self.A[index]
    

    def swap_columns(self, col1, col2):
        for row in self.A:
            row[col1], row[col2] = row[col2], row[col1]
    

def caldet(matrix,wsp = 1):
    
    #Create matrix of determinants
    C = Matrix((matrix.size()[0] - 1, matrix.size()[1] - 1))
    
    #create2x2 matrix
    m2x2 = Matrix((2,2))
    
    
    
    i = 1
    j = 0
    k = 0
    
    
    #if first elem in matrix is 0 swap col to provide from dividing by 0 
    if matrix[0][0] == 0:
        for i in range(matrix.size()[0]):
            if matrix[0][i] != 0:
                matrix.swap_columns(0,i)
                wsp = wsp * (-1)
                break
        
    wsp = wsp * matrix[0][0] ** (matrix.size()[0] - 2)
    
    if matrix.size()[1] == 2:
        return calcdet2x2(matrix)/wsp
    
    while i < matrix.size()[1]:
        
        #if matrix was shorten to vector - break
        try:
            m2x2[0][0] = matrix[0][0]
            m2x2[1][0] = matrix[1][0]
            m2x2[0][1] = matrix[0][i]
            m2x2[1][1] = matrix[1][i]
            
            C[k][j] = calcdet2x2(m2x2)
            j += 1
            i += 1
            
            if i == matrix.size()[1]:
                matrix.delete_row(1)
                k += 1
                i = 1
                j = 0
                
        except IndexError:
            break    
    
    return caldet(C,wsp)        


def calcdet2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

m1 = Matrix([[5,1,1,2,3],[4,2,1,7,3],[2,1,2,4,7],[9,1,0,7,0],[1,4,7,2,2]])
m2 = Matrix([[0,1,1,2,3],[4,2,1,7,3],[2,1,2,4,7],[9,1,0,7,0],[1,4,7,2,2]])

print(caldet(m1))
print(caldet(m2))