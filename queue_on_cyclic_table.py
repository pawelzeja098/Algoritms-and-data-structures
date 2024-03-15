class Queue:
    
    def __init__(self,size = 5) -> None:
        self.tab = [None for i in range(size)]
        self.head = -1 #index to read
        self.tail = -1 #index to save
        self.size = size
        # self.curr_size = self.size()

    
    def realloc(self, size):
        oldSize = len(self.tab)
        self.tab = [self.tab[i] if i<oldSize else None  for i in range(size)]
        self.size = size
    
    def enqueue(self,data):
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.tab[self.tail] = data
            self.tail += 1
        
        
        else:
            # self.tail = (self.tail + 1) % self.size
            # self.tab[self.tail] = data
            # self.tail += 1
            if self.tail == len(self.tab):  # Check if array is full
                self.realloc(len(self.tab) * 2)  # Double the size of the array
            self.tab[self.tail] = data
            self.tail += 1

    def is_empty(self) -> bool:
        if self.tab[self.head] is None:
            return True
        return False

    def peek(self):
        print(self.tab[self.head])

    
    def dequeue(self):
        if self.head == -1:
            print('Can`t remove from empty queue')
            return
        x = self.tab[self.head]
        # print(self.tab[self.head])
        self.tab[self.head] = None
        self.head += 1
        return x
        


    def __str__(self):
        pass
    
    def display(self):
        print(self.tab)
        # print(len(self.tab))
        
    # def size(self):
    #     q_size = self.head - self.tail
    #     return q_size

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.display()
    queue.dequeue()
    
    queue.peek()
    queue.display()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.display()

    elem = queue.dequeue()
    while elem is not None:
        print(elem)
        elem = queue.dequeue()
    queue.display()
    print(queue.is_empty())


main()