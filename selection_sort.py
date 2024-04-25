import time
import random
class Elem:
    def __init__(self,priority,data) -> None:
        
        self.__data = data
        self.__priority = priority
    
    def __lt__(self,other):
        return self.__priority < other.__priority

    def __gt__(self,other):
        return self.__priority > other.__priority
    
    def __repr__(self):
        return (f"{self.__priority} : {self.__data}")

class Selsort:

    def swap(tab):
        for i in range(len(tab)):
            min_idx = i
            for j in range(i + 1,len(tab)):
                if tab[j] < tab[min_idx]:
                    min_idx = j
            
            tab[i], tab[min_idx] = tab[min_idx], tab[i]
        return tab     

    def shift(tab):
        for i in range(len(tab)):
            min_idx = i
            for j in range(i + 1,len(tab)):
                if tab[j] < tab[min_idx]:
                    min_idx = j
            min_elem = tab.pop(min_idx)
            tab.insert(i,min_elem)

    def print_tab(tab):
        print ('{', end=' ')
        print(*tab[:len(tab)], sep=', ', end = ' ')
        print( '}')

def main():
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]    
    tab = [ Elem(key, value) for key,value in  data]

    tab2 = tab.copy()
    
    Selsort.swap(tab)
    Selsort.print_tab(tab)

    Selsort.shift(tab2)
    Selsort.print_tab(tab2)

    

def test2():
    tab = []
    while len(tab) < 10000:
        tab.append(int(random.random() * 100))
    
    tab_t_s = [Elem(key,'A') for key in tab]
    tab_t_s2 = tab_t_s.copy()
    t_start = time.perf_counter()
    # testowana metoda
    Selsort.swap(tab_t_s)
    t_stop = time.perf_counter()
    c_t_swap = t_stop - t_start
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    

    t_start = time.perf_counter()
    # testowana metoda
    Selsort.shift(tab_t_s)
    t_stop = time.perf_counter()
    c_t_shift = t_stop - t_start
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))



    
main()
test2()

    
