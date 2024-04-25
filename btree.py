class Node():
    def __init__(self) -> None:
        self.keys = []
        self.children = []
        self.size = 0
    

class Btree:
    def __init__(self,max_child) -> None:
        self.root = None
        self.max_child = max_child
    
    def insert(self,key):
        
        if self.root is None:
            node = Node()
            node.keys.append(key)
            self.root = node
            return
        
        curr = self.root

        for k in curr.keys:
            if k > key:
                if not curr.children:
                    self.add_to_node(key,curr)
                    return
                else:
                    self.insert(curr.children[0])
        
        if not curr.children:
            self.add_to_node(key,curr)
            return
        self.insert(curr.children[-1])

    def add_to_node(self,key,curr = None):
        idx = 0
        for i in curr.keys:
            if i > key:
                curr.keys.insert(idx,key)
                break
            idx += 1
        curr.keys.insert(idx,key)




        if len(curr.keys) == self.max_child:
            idx = self.max_child // 2
            key_p = curr.keys.pop(idx)
            left_child = Node()
            left_child.keys.extend(curr.keys[:idx])
            del curr.keys[:idx]
            right_child = Node()
            right_child.keys.extend(curr.keys[:])
            curr.keys.append(key_p)
            curr.children.append(left_child)
            curr.children.append(right_child)
            return key_p
        
        return None









            

    def print_tree(self):
        pass




def main():
    tree = Btree(4)
    keys = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for i in keys:
        tree.insert(i)
    




main()