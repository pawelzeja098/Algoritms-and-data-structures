import time

def rekur_var(P,T,i,j):
    if i == 0:
        return j
    if j == 0:
        return i
    switch = rekur_var(P,T,i-1,j-1) + (P[i]!=T[j])
    place = rekur_var(P,T,i,j-1) + 1
    delete = rekur_var(P,T,i-1,j) + 1

    min_cost = min(switch,place,delete)

    return min_cost


def pd_var(P,T,n,m,D,Parents):
    
    for i in range(1,n + 1):
        for j in range(1,m + 1):

            switch = D[i-1][j-1] + (P[i -1]!=T[j - 1])
            place = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            
            min_cost = min(switch,place,delete)
            D[i][j] = min_cost

            if min_cost == switch:
                if P[i-1] == T[j-1]:
                    Parents[i][j] = 'M'
                else:
                    Parents[i][j] = 'S'
            elif min_cost == place:
                Parents[i][j] = 'I'
            else:
                Parents[i][j] = 'D'

            
            
    
    return D[n][m]

def reconstruct_path(Parents, n, m):
    i, j = n, m
    path = []
    
    while i > 0 or j > 0:
        if Parents[i][j] == 'M' or Parents[i][j] == 'S':
            path.append(Parents[i][j])
            i -= 1
            j -= 1
        elif Parents[i][j] == 'I':
            path.append('I')
            j -= 1
        elif Parents[i][j] == 'D':
            path.append('D')
            i -= 1
    
    path.reverse()
    return ''.join(path)

def string_compare(P, T, m, n, D, Parents):
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            switch = D[i-1][j-1] + (P[i-1] != T[j-1])
            place = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            
            min_cost = min(switch, place, delete)
            D[i][j] = min_cost

            if min_cost == switch:
                if P[i-1] == T[j-1]:
                    Parents[i][j] = 'M'
                else:
                    Parents[i][j] = 'S'
            elif min_cost == place:
                Parents[i][j] = 'I'
            else:
                Parents[i][j] = 'D'
    
   
    goal_index = goal_cell(D)
    
    return D[n][goal_index], goal_index

def goal_cell(D):
    
    first_row = D[1] 
    min_value = min(first_row)
    goal_index = first_row.index(min_value)
    return goal_index

def lcs_var(P, T, n, m, D, Parents):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if P[i - 1] == T[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
                Parents[i][j] = 'M'
            elif D[i - 1][j] >= D[i][j - 1]:
                D[i][j] = D[i - 1][j]
                Parents[i][j] = 'U'
            else:
                D[i][j] = D[i][j - 1]
                Parents[i][j] = 'L'
    return D[n][m]

def reconstruct_lcs(P, Parents):
    n = len(Parents) - 1
    m = len(Parents[0]) - 1
    lcs = []
    
    while n > 0 and m > 0:
        if Parents[n][m] == 'M':
            lcs.append(P[n - 1])
            n -= 1
            m -= 1
        elif Parents[n][m] == 'U':
            n -= 1
        else:
            m -= 1
    
    lcs.reverse()
    return ''.join(lcs)

def main():
    T = ' kot'
    P = ' pies'
    i = len(P) - 1
    
    j = len(T) - 1
    
    
    nb = rekur_var(P,T,i,j)
    
    print(f'Minimalny koszt rekur: {nb}')
    
    
    
    P = "biały autobus"
    T = "czarny autokar"
    i = len(P)
    j = len(T)

    
    D = (i,j)
    D = [[0 for _ in range(D[1] + 1)] for _ in range(D[0] +1)]
    for a in range(i + 1):
        D[a][0] = a
    for b in range(j + 1):
        D[0][b] = b

    

    Parents = (i,j)
    Parents = [['X' for _ in range(Parents[1] + 1)] for _ in range(Parents[0] + 1)]
    for a in range(i):
        Parents[a][0] = 'D'
    for b in range(j):
        Parents[0][b] = 'I'

    Parents[0][0] = 'X'
    
    
    cost = pd_var(P,T,i,j,D,Parents)
    
    print(f"Minimalny koszt pd: {cost}")
    



    P = "thou shalt not"
    T = "you should not"
    i = len(P)
    j = len(T)

    
    D = [[0 for _ in range(j + 1)] for _ in range(i + 1)]
    for a in range(i + 1):
        D[a][0] = a
    for b in range(j + 1):
        D[0][b] = b

    
    Parents = [['X' for _ in range(j + 1)] for _ in range(i + 1)]
    for a in range(1, i + 1):
        Parents[a][0] = 'D'
    for b in range(1, j + 1):
        Parents[0][b] = 'I'

    Parents[0][0] = 'X'

    pd_var(P, T, i, j, D, Parents)
    
    path = reconstruct_path(Parents, i, j)
    print("Ścieżka przekształceń:", path)




    P = "ban"
    T = "mokeyssbanana"

    
    i = len(P)
    j = len(T)
    D = [[0 for _ in range(j + 1)] for _ in range(i + 1)]
    for a in range(i + 1):
        D[a][0] = a

    
    Parents = [['X' for _ in range(j + 1)] for _ in range(i + 1)]
    for a in range(1, i + 1):
        Parents[a][0] = 'D'
    for b in range(1, j + 1):
        Parents[0][b] = 'I'

    Parents[0][0] = 'X'
    cost, index = string_compare(P, T,j,i, D, Parents)
    
    print("Indeks pierwszej litery szukanego wzorca w przeszukiwanym napisie:", index)

    T = 'democrat'
    P = 'republican'
    i = len(P)
    j = len(T)
    
    D = [[0 for _ in range(j + 1)] for _ in range(i + 1)]
    Parents = [['X' for _ in range(j + 1)] for _ in range(i + 1)]
    
    
    lcs_var(P, T, i, j, D, Parents)
   
    lcs = reconstruct_lcs(P, Parents)
    print("Najdłuższa wspólna sekwencja:", lcs)

    T = ' 243517698'
    P = ''.join(sorted(T))
    
    i = len(P)
    j = len(T)
    
    D = [[0 for _ in range(j + 1)] for _ in range(i + 1)]
    Parents = [['X' for _ in range(j + 1)] for _ in range(i + 1)]
    
    lcs_var(P, T, i, j, D, Parents)

    lcs = reconstruct_lcs(P, Parents)
    print("Najdłuższa podsekwencja monotoniczna:", lcs)

main()