import random

class Elem:
    def __init__(self,key,value,level) -> None:
        self.key = key
        self.value = value
        self.level = level
        self.next = [None for i in range(self.level)]



      

class Skiplist:
    def __init__(self,max_height) -> None:
        self.max_level = max_height
        self.head = Elem(None, None, max_height)

    def randomLevel(self,p):
        lvl = 1   
        while random.random() < p and lvl < self.max_level:
                lvl = lvl + 1
        return lvl 

    def search(self):
        pass

    def insert(self,key,value):
        lvl = self.randomLevel(0.5)
        node = Elem(key,value,lvl)
        prev = [self.head for i in range(self.level)]
        curr = self.head
        for level in range(self.max_level -1, -1, -1):
            while curr[level] and curr[level].key < key:
                curr = curr.next[level]
            prev[level] = curr
        curr = curr.next[0]
        if curr and curr.key == key:
            pass

    def remove(self):
        pass

    def __str__(self) -> str:
        pass
    
    def displayList_(self):
        node = self.head.tab[0]  # pierwszy element na poziomie 0
        keys = [ ]                        # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()

def main():

    random.seed(42)

    skip_list = Skiplist(5)
