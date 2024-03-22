#tyle prób szukania ile size tablicy
class Hash_table:
    def __init__(self,size,c1 = 1,c2 = 0) -> None:
        self.tab = [None for i in range(size)]
        self.size = size

    def hashing(self,elem):
        print(elem.value)
        if isinstance(elem.value, str):
            elem.value = ord(elem.value)
        print(elem.value)
    
    
    # def solve_collision()
    
    def search(self,key):
        pass
        
    def insert(self,elem):
        # print(elem.key)
        index = self.hashing(elem)

    def remove(self,key):
        pass

    def __str__(self) -> str:
        pass

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
    test1()
            

main()