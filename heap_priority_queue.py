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

class Pqueue:
    def __init__(self) -> None:
        self.queue = []
        self.heap_size = 0

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]


    def enqueue(self,elem):
        heigth = self.heap_size
        if self.is_empty() is True:
            self.queue.append(elem)
            self.heap_size += 1
            return
        self.queue.append(elem)
        heigth += 1
        last = self.queue[-2]
        if last > elem:
            self.heap_size += 1
            return
        
        idx = heigth - 1
        curr = self.queue[self.parent(idx)]
        while idx != 0 and  curr < elem:
            
            
            self.queue[self.parent(idx)] = elem
            self.queue[idx] = curr
            idx = self.parent(idx)
            curr = self.queue[self.parent(idx)]
        self.heap_size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        deq = self.queue[0]
        self.queue[0] = self.queue[self.heap_size - 1]
        self.queue = self.queue[:-1]
        self.heap_size -= 1
        self.fix_sort_heap(0)
        return deq

    def fix_sort_heap(self,idx):
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        largest = idx
        if left_idx < self.heap_size and self.queue[left_idx] > self.queue[idx]:
            largest = left_idx
        if right_idx < self.heap_size and self.queue[right_idx] > self.queue[idx]:
            if self.queue[right_idx] > self.queue[left_idx]:
                largest = right_idx
        if largest != idx:
            temp = self.queue[idx]
            self.queue[idx] = self.queue[largest]
            self.queue[largest] = temp
            self.fix_sort_heap(largest)


    def left(self,idx):
        return idx * 2 + 1
        

    def right(self,idx):
        return idx * 2 + 2

    def parent(self,idx):
        if idx == 0:
            return 0
        return (idx) // 2

    def print_tab(self):
        print ('{', end=' ')
        print(*self.queue[:len(self.queue)], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<len(self.queue):           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.queue[idx] if self.queue[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)
    

def main():
    queue = Pqueue()
    priority_list = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    values = list("GRYMOTYLA")
    for i in range(len(priority_list)):
        elem = Elem(priority_list[i],values[i])
        queue.enqueue(elem)
    queue.print_tree(0,0)
    queue.print_tab()
    
    deq = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(deq)
    deq = 0
    while deq != None:
        deq = queue.dequeue()
        if deq != None:
            print(deq)
    queue.print_tab()
           

    


main()