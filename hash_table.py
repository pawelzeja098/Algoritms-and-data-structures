#tyle prób szukania ile size tablicy
class Hash_table:
    def __init__(self,size,c1 = 1,c2 = 0) -> None:
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hashing(self,elem):
        
        if isinstance(elem.key, str):
            for i in elem.key:
                key = 0
                

                key += ord(i)
                elem.key = key
        
        return elem.key % self.size
    
    
    def solve_collision(self,elem):
        idx = self.hashing(elem)
        n_idx = (idx + self.c1 * elem.key + self.c2 * elem.key ** 2) % self.size
        if self.tab[n_idx] is None:

            return n_idx
        i = 0
        while i <= self.size:
            n_idx = (n_idx + self.c1 * elem.key + self.c2 * elem.key ** 2) % self.size
            if self.tab[n_idx] is None:
                return n_idx
            i += 1
        return None
    def search(self,key):
        
        for elem in self.tab:
            if elem is not None and elem.key == key:
                print(f'Dana o kluczu {key} to {elem.value}')
                return elem.value
        print('Brak danej o podanym kluczu')
        return None

        
    def insert(self,elem):
        # print(elem.key)
        
        #check if key is already in table
        for elem_in_tab in self.tab:
            if  elem_in_tab is not None and elem_in_tab.key == elem.key:
                elem_in_tab.value = elem.value
                return

        idx = self.hashing(elem)
        if self.tab[idx] is not None:
            n_idx = self.solve_collision(elem)
            if n_idx is not None:
                self.tab[n_idx] = elem
                return
            print("Brak miejsca")
            return
        self.tab[idx] = elem

    def remove(self,key):
        for elem in self.tab:
            if  elem is not None and elem.key == key:
                self.tab[key] = None
                return

    def __str__(self) -> str:
        res = '{'
        for elem in self.tab:
            if elem is not None:
                res += f"{elem.key}" + ':' + f"{elem.value}" + ','
            else:
                res += 'None' + ','
        return res + '}'

    def display(self):
        print(self.tab)
class Elem():
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        

def main():
    def test1():
        tab = Hash_table(13)
        i = 1
        data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        
        while i <= 15:
            if i == 6:
                i = 18
                elem = Elem(i,data[5])
                i = 7
                tab.insert(elem)

            if i == 7:
                i = 31
                elem = Elem(i,data[6])
                i = 8
                tab.insert(elem)

            elem = Elem(i,data[i - 1])
            i += 1
            tab.insert(elem) 
        print(tab)
        tab.search(5)
        tab.search(14)
        elem = Elem(5,'Z')
        tab.insert(elem)
        tab.search(5)
        tab.remove(5)
        print(tab)
        tab.search(31)

        elem = Elem('W','test')
        tab.insert(elem)

    test1()
            

main()

# a = 'abcd'
# for i in a:
#     print(i)