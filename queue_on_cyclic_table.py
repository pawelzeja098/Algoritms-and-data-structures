class Queue:
    
    def __init__(self,size = 5) -> None:
        self.tab = [None for i in range(size)]
        self.head = -1 #index to read
        self.tail = -1 #index to save
        self.max_size = size
        # self.curr_size = self.size()

    
    # def realloc(tab, size):
    #     oldSize = len(tab)
    #     return [tab[i] if i<oldSize else None  for i in range(size)]
    
    def enqueue(self,data):
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.tab[self.tail] = data
            self.tail += 1
        
        
        else:
            self.tab[self.tail] = data
            self.tail += 1

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        return False

    def peek(self):
        print(self.tab[self.head])

    
    def dequeue(self):
        print(self.tab[self.head])
        self.tab[self.head] = None
        self.head += 1


    def __str__(self):
        pass
    
    def display(self):
        print(self.tab)
        
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


main()