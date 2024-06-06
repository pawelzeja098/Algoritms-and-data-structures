import time


def naive_method(S,W):
    t_start = time.perf_counter()
    m = 0 #tekst
    i = 0 #wzorzec
    found_patt = 0
    nb_comp = 0
    dot = '.'
    while m < len(S):
        nb_comp += 1
        if S[m]  ==  W[i]:
            m += 1
            i += 1
            if i == 4:
                if S[m] == dot:
                    found_patt += 1
                    i = 0
                else:
                    i = 0
                    m += 1
        else:
            i = 0
            m += 1
    
    t_stop = time.perf_counter()
    # print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return found_patt, nb_comp
            

def rabin_karp(S,W):

    t_start = time.perf_counter()
    found_patt = 0
    nb_comp = 0
    
    hw = hash(W)
    for m in range(len(S) - len(W) + 1):
        hs = hash(S[m:m + len(W)])
        nb_comp += 1
        if hs == hw:
            
            if S[m:m + len(W) ] == W:
                found_patt += 1
            
        
    t_stop = time.perf_counter()
    # print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return found_patt, nb_comp


def rabin_karp2(S,W):
    d = 256
    q = 101
    t_start = time.perf_counter()
    found_patt = 0
    nb_comp = 0
    col = 0 
    hw = hash(W)

    h = 1
    for i in range(len(W) - 1):
        h = (h * d) % q

    hs = hash(S[:len(W)])

    for m in range(len(S) - len(W) + 1):
        
        nb_comp += 1
        if hs == hw:
            if S[m:m + len(W)] == W:
                found_patt += 1
            else:
                col += 1
        
        if m < len(S) - len(W):
            hs = (d * (hs - ord(S[m]) * h) + ord(S[m + len(W)])) % q
            if hs < 0:
                hs += q
        
    t_stop = time.perf_counter()
    # print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return found_patt, nb_comp, col

def hash(word):
    d = 256 
    q = 101

    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time.'
    
    naive = naive_method(S,W)
    rk1 = rabin_karp(S,W)
    rk2 = rabin_karp2(S,W)

    print(f'{naive[0]};{naive[1]}')
    print(f'{rk1[0]};{rk1[1]}')
    print(f'{rk2[0]};{rk2[1]};{rk2[2]}' )
main()