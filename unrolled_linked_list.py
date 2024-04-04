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
        count = 0
        for tab in self.tab:
            for val in tab.node:
                if val:
                    count += 1
                    if count - 1 == idx:
                        return val

    
    def insert(self,idx,data):
        
        if not self.tab:
            current = Elem()
            self.head = current
            self.tab.append(current)
            self.nbNode += 1
        
        if idx < self.size and self.head.node[idx] is None:
            
            self.head.node[idx] = data
            self.head.nbElem += 1
            return
        # if self.head.nbElem == self.size:
        #     self.tail = Elem()
        #     self.tab.append(self.tail)
        #     self.nbNode += 1
        
        node_idx = idx // self.size
        
        if node_idx < len(self.tab):
            current = self.tab[node_idx]
            if current.node[idx % self.size]:
                if current.nbElem == self.size:
                    new_n = Elem()
                    self.tab.insert(node_idx + 1,new_n)
                    for i in range(self.size // 2):
                        new_n.node[i] = current.node[self.size // 2 + i]
                        current.node[self.size // 2 + i] = None
                    if idx > self.size:    
                        new_n.node[idx] = data
                        new_n.nbElem += 1
                        return
                        
                    else:
                        elem = current.node[idx]
                        current.node[idx] = None
                        current.node[idx + 1:] = current.node[idx:-1]
                        current.node[idx] = data
                        current.node[idx + 1] = elem
                        current.node[idx] = data
                        current.nbElem += 1
                        return

                else:
                    elem = current.node[idx % self.size]
                    current.node[idx % self.size] = None
                    current.node[idx % self.size + 1:] = current.node[idx % self.size:-1]
                    current.node[idx % self.size] = data
                    current.node[idx % self.size + 1] = elem
                    return
        
        i = 0
        while node_idx > 0:
            i += 1
            node_idx -= 1
        try:
            current = self.tab[i]
        except IndexError:
            current = Elem()
            self.tab.append(current)
            self.nbNode += 1
            
        
        current.node[idx % self.size] = data
        current.nbElem += 1
        return


            
        # current = self.head
        # if self.head.nbElem == self.size:
        #     self.tail = Elem() 
        # if current.nbElem == self.size:
        #     current.next = Elem()
        # node_idx = idx // self.size
        # # while node_idx > 0:
        # prev = None
        # i = 1
        # curr = self.tail
        # while curr is not None and node_idx > 0:
            
        #     # current = self.tab[i]
        #     prev = current
        #     curr = self.tab[i]
        #     node_idx -= 1
        #     i += 1

        # if curr:
        #     self.tail = curr.node[idx % self.size]
        # if prev:
        #     current = prev

        # if idx < self.size and current.node[idx] is None:
            
        #     self.head.node[idx] = data
        #     self.head.nbElem += 1
        #     return
        
        
        
        # if self.tail is None:
        #     self.tail = Elem()
        #     # current.next = None
        #     self.nbNode += 1
        #     self.tab.append(self.tail)
        #     # self.tail = current
        #     self.tail.node[idx % self.size] = data
        #     return

        # else:
        #     if self.tail.node[idx % self.size] is not None:
        #           self.tail.node[idx % self.size] = data
        #           return 



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

        # if idx > self.size * len(self.tab):
        #     current.node = self.tab[-1]
        #     for i in current.node:
        #         if i is None:
        #             current.node[i] = data
        #             current.nbElem += 1
        #             return
        #     new_node = Elem()
        #     new_node.node[0] = data
        #     self.nbNode += 1
        #     self.tab.append(new_node)
        #     return

            

        # node_idx = idx // self.size
        # current = self.tab[node_idx]
        # # while current.next is not None:
        # #     current = current.next
        # new_node = Elem()
        # self.nbNode = 1

        # for i in range(self.size // 2):
        #     new_node.elem[i] = current.elem[self.size // 2 + i]
        #     current.elem[self.size // 2 + i] = None

        # if idx > self.size:    
        #     new_node.elem[idx] = data
        #     new_node.nbElem += 1
        #     current.next = new_node 
        # else:
        #     current.elem[idx] = data
        #     current.nbElem += 1
        
        # a = 5
    
    def display(self):
        for idx, elem in enumerate(self.tab):
            print(f"Node {idx}: {elem.node}")

    
    def delete(self,idx):
        count = 0
        c_tab = 0
        
        for tab in self.tab:
            c_tab += 1
            c_val = 0
            for val in tab.node:
                c_val += 1 
                if val:
                    count += 1
                    if count - 1 == idx:
                        curr = self.tab[c_tab - 1]
                        curr.node[c_val - 1] = None
                        return
                        


def main():

    size = 6
    tab = Unrolled_list(size)
    for i in range(1,10):
        tab.insert(i-1,i)
    tab.display()
    print(tab.get(4))   
    tab.insert(1,10)
    tab.display()
    tab.insert(8,11)
    tab.display()
    tab.delete(1)
    tab.delete(2)
    tab.display()

main()