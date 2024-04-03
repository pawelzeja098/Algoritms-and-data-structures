class Elem:
    def __init__(self,size = 6) -> None:
        self.node = [None for i in range(size)]
        self.nbElem = 0
        self.next = None
        

class Unrolled_list:
    def __init__(self,size = 6) -> None:
        # self.tab = Elem()
        self.tab = []
        self.size = size
        self.head = None
        self.tail = None
        self.nbNode = 0

        

    def get(self,idx):
        return self.tab[idx]

    
    def insert(self,idx,data):
        
        if not self.tab:
            current = Elem()
            self.head = current.node
            self.tab.append(current)
            self.nbNode += 1
        
        current = self.tab[0]
        
        node_idx = idx // self.size

        prev = None
        i = 0
        while current is not None and node_idx > 0:
            
            current = self.tab[i]
            prev = current
            current = current.next
            node_idx -= 1

        current = prev

        if idx < self.size and current.node[idx] is None:
            
            current.node[idx] = data
            current.nbElem += 1
            return
        
        
        
        if current is None:
            current = Elem()
            current.next = None
            self.nbNode += 1
            self.tab.append(current)

            current.node[idx % self.size] = data
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

        if idx > self.size * len(self.tab):
            current.node = self.tab[-1]
            for i in current.node:
                if i is None:
                    current.node[i] = data
                    current.nbElem += 1
                    return
            new_node = Elem()
            new_node.node[0] = data
            self.nbNode += 1
            self.tab.append(new_node)
            return

            

        node_idx = idx // self.size
        current = self.tab[node_idx]
        # while current.next is not None:
        #     current = current.next
        new_node = Elem()
        self.nbNode = 1

        for i in range(self.size // 2):
            new_node.elem[i] = current.elem[self.size // 2 + i]
            current.elem[self.size // 2 + i] = None

        if idx > self.size:    
            new_node.elem[idx] = data
            new_node.nbElem += 1
            current.next = new_node 
        else:
            current.elem[idx] = data
            current.nbElem += 1
        
        a = 5
    
    def display(self):
        print(self.tab)

    
    def delete(self):
        pass


def main():

    size = 6
    tab = Unrolled_list(size)
    for i in range(1,10):
        tab.insert(i-1,i)
    tab.display()   

main()