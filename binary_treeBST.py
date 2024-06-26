class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.child_right = None
        self.child_left = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,key,value) -> None:
        #create root
        if not self.root:
            node = Node(key,value)
            self.root = node
            return
        
        


        node = Node(key,value)
        #create first child to root
        if self.root.child_left is None and self.root.child_right is None:
            if key < self.root.key:
                self.root.child_left = node
                return

            else:
                self.root.child_right = node
                return
        
        #change root value if the same key as root
        if node.key == self.root.key:
            self.root = node
            return

        #choose path from root
        elif node.key < self.root.key:
            next_n = self.root.child_left
            if next_n == None:
                self.root.child_right = node
        else:
            next_n = self.root.child_right
            if next_n == None:
                self.root.child_right = node
                return


        

        #look for placement
        while next_n:
            left = False
            right = False
            #left child
            if node.key < next_n.key:
                current = next_n
                next_n = current.child_left
                left = True
            #change value for the same key
            elif node.key == next_n.key:
                next_n.value = node.value
                return
            #right child
            else:
                current = next_n
                next_n = current.child_right
                right = True

        
        if left:
            current.child_left = node
        if right:
            current.child_right = node


    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.child_right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.child_left, lvl+5)
    
    def search(self,key,node = None):
        
        if node is None:
            node = self.root

        if key == node.key:
            return node.value

        if key < node.key:
            return self.search(key, node.child_left)
        elif key > node.key:
            return self.search(key, node.child_right)

        return None
        
    def search_to_delete(self,key,node = None, prev = None, left = False):

        if node is None:
            node = self.root

        if key == node.key:
            return node, prev, left

        if key < node.key:
            return self.search_to_delete(key, node.child_left,node,True)
        elif key > node.key:
            return self.search_to_delete(key, node.child_right,node,False)

        return None


    def delete(self,key,node = None,prev = None,left = False):
        
        if node == None:
            node, prev, left = self.search_to_delete(key)


        if node.child_left == None and node.child_right == None:
            if left:
                prev.child_left = None
                return
            else:
                prev.child_right = None
                return
        
        elif node.child_right == None or node.child_left == None:
            if node == prev.child_left:
                
                if node.child_right:
                    prev.child_left = node.child_right
                else:
                    prev.child_left = node.child_left
                
                
                return
            else:
                
                if node.child_right:
                    prev.child_right = node.child_right
                else:
                    prev.child_right = node.child_left
                
                return
        else:
            curr = node.child_right
            i = 0
            prev1 = None
            while curr is not None:
                prev = prev1
                prev1 = curr
                curr = curr.child_left
                i += 1
                
            node.key = prev1.key
            node.value = prev1.value
            if i != 1:
                return self.delete(prev1.key,prev1,prev,True)
            else:
                return self.delete(prev1.key,prev1,node,False)
            




    def print_tree_list(self):
        self.print_tree_in_order(self.root)
        print("\n")
        

    def print_tree_in_order(self, node):
        if node is not None:
            self.print_tree_in_order(node.child_left)
            print(f"{node.key} {node.value}", end=", ")
            self.print_tree_in_order(node.child_right)


    
    def count_length(self,node):
        curr = node
        length = 0
        while curr is not None:
            
            if curr.child_left and curr.child_right:
                
                length += 1
                lengthl_l , lengthl_r = self.branching(length,curr)
                if lengthl_l >= lengthl_r:
                    length += lengthl_l
                else:
                    length += lengthl_r

                return length
            
            elif curr.child_left:
                curr = curr.child_left
                length += 1
            
            else:
                curr = curr.child_right
                length += 1
            
    def branching(self,length,node):
        curr_l = node.child_left
        curr_r = node.child_right
        length_l = length
        length_r = length
        while curr_l:
            if curr_l.child_left and curr_l.child_right:
                length_l += 1
                length_l , length_r = self.branching(length_l,curr_l)
                return length_l, length_r
            elif curr_l.child_left:
                curr_l = curr_l.child_left
                length_l += 1
            else:
                curr_l = curr_l.child_right
                length_l += 1

        while curr_r:
            if curr_r.child_left and curr_r.child_right:
                length_r += 1

                length_l , length_r = self.branching(length_r,curr_r)

            elif curr_r.child_left:
                curr_r = curr_r.child_left
                length_r += 1
            else:
                curr_r = curr_r.child_right
                length_r += 1
        
        return length_l, length_r



    
    def height(self,node = None):
        if not node:
            node = self.root
        if node.child_left:
            length_l = self.count_length(node.child_left)
        
        if node.child_right:
            length_r = self.count_length(node.child_right)
        
        if length_l >= length_r:
            return length_l
        else:
            return length_r


        
        




def main():
    
    data = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}

    keys = [50,15,62,5,20,58,91,3,8,37,60,24]
    

    tree = Tree()
    for i in keys:
        tree.insert(i,data[i])
    tree.print_tree()
    tree.print_tree_list()
    
    print(tree.search(24))
    tree.insert(20,'AA')
    

    tree.insert(6,'M')
    
    tree.delete(62)
    
    tree.insert(59,'N')
    tree.insert(100,'P')
    
    tree.delete(8)
    
    tree.delete(15)
    
    
    tree.insert(55,'R')
    
    tree.delete(50)
    
    tree.delete(5)
    
    tree.delete(24)
    print(f"maksymalna wysokość drzewa:{tree.height()}")
    tree.print_tree_list()
    tree.print_tree()



main()