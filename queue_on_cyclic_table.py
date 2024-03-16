class Queue:
    
    #construct the queue
    def __init__(self,size = 5) -> None:
        self.tab = [None for i in range(size)]
        self.head = -1 #index to read
        self.tail = -1 #index to save
        self.size = size
        

    #double the size and realloc data in queue
    def realloc(self, size):
        oldSize = len(self.tab)
        self.tab = [self.tab[i] if i<oldSize else None  for i in range(size)]
        
        curr_val = []
        curr_val = self.tab[self.head:self.size]
        self.tab[self.size + self.head:] = curr_val
        i = self.head
        while i < self.size:
            self.tab[i] = None
            i += 1
        self.tail = self.head
        self.head += self.size
        self.size = size
    
    #Add to the end of queue
    def enqueue(self,data):
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.tab[self.tail] = data
            self.tail += 1
        else:
            if self.tail == self.head:  # Check if queue is full
                self.realloc(len(self.tab) * 2)  # Double the size of the array
            self.tab[self.tail] = data
            self.tail = (self.tail + 1) % self.size


    def is_empty(self) -> bool:
        if self.tab[self.head] is None:
            return True
        return False

    def peek(self):
        print(self.tab[self.head])

    #remove from queue
    def dequeue(self):
        if self.tab[self.head] is None:
            return None
        x = self.tab[self.head]
        self.tab[self.head] = None
        self.head = (self.head + 1) % self.size
        print(x)
        return x
        
    def __str__(self):
        res = '['
        indx = self.head
        first_iteration = True
        while self.tab[indx] is not None:
            if not first_iteration:
                res += ' '  
            res += str(self.tab[indx])
            first_iteration = False
            indx = (indx + 1) % self.size
        res += ']'  
        return res


    #Used to testing
    # def display(self):
    #     print(self.tab)

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    queue.dequeue()
    
    queue.peek()
    
    print(queue)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    
    print(queue)

    elem = queue.dequeue()
    while elem is not None:
        elem = queue.dequeue()
    print(queue)
    


main()