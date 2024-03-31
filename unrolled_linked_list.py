class Elem:
    def __init__(self,size = 5) -> None:
        self.tab = [None for i in range(size)]
        self.nbElem = 0
        self.next = None
        pass

class Unrolled_list:
    def __init__(self,size = 5) -> None:
        self.tab = Elem()
        self.size = size
        

    def get(self,idx):
        return self.tab[idx]

    
    def insert(self,data,idx):
        if self.tab[idx] is None:
            self.tab[idx] = data
            self.tab.nbElem += 1
            return
        # if self.head == None:
        #     self.tab[idx] = data
        #     self.head = idx
        #     self.tail = idx

        # if idx == self.size:

        #     tab = Elem(self.size + 1)
        #     for i in range(self.size):
        #         tab[i] = self.tab[i]
        #     tab[idx] = data
        #     self.tab = tab
        #     self.size += 1
        #     return    

        tab = Elem(self.size)
        x = self.size - idx
        for i in range(self.size // 2):
            tab[i] = self.tab[self.size // 2 + i]

            
        tab[idx] = data
        for i in range()


    
    def delete(self):
        pass



