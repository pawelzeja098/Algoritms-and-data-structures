class Node():
    def __init__(self,max_child) -> None:
        self.keys = []
        self.children = [None for i in range(max_child)]
        self.size = 0
    

class Btree:
    def __init__(self,max_child) -> None:
        self.root = None
        self.max_child = max_child
        
    
    def insert(self,key,c_idx = None,curr = None,parent = None):
        
        if self.root is None:
            node = Node(self.max_child)
            node.keys.append(key)
            self.root = node
            return
        if curr is None:
            curr = self.root

        for k in curr.keys:
            if k > key:
                if all(elem is None for elem in curr.children):
                    self.add_to_node(key,c_idx,curr,parent)
                    
                    return
                else:
                    parent = curr
                    self.insert(key,0,curr.children[0],parent)
                    return
        
        if all(elem is None for elem in curr.children):
            self.add_to_node(key,c_idx,curr,parent)
            return
        idx = 0
        for child in curr.children:
            if child is None:
                parent = curr
                c_idx = idx - 1
                self.insert(key,idx - 1,curr.children[idx - 1],parent)

                return
            idx += 1
        
    def add_to_node(self,key,c_idx = None,curr = None,parent = None):
        idx = 0
        inserted = False
        for i in curr.keys:
            if i > key:
                curr.keys.insert(idx,key)
                inserted = True
                break
            idx += 1
        if not inserted:
            curr.keys.insert(idx,key)




        if len(curr.keys) == self.max_child:
            idx = self.max_child // 2
            key_p = curr.keys.pop(idx)
            left_child = Node(self.max_child)
            left_child.keys.extend(curr.keys[:idx])
            del curr.keys[:idx]
            right_child = Node(self.max_child)
            right_child.keys.extend(curr.keys[:])
            del curr.keys[:]
            if parent:
                parent.keys.append(key_p)
                # self.add_to_node(key_p,parent)
                if len(parent.keys) == self.max_child - 1:
                    self.add_to_node(key_p,None,parent)
                    return
                
                parent.children[c_idx]=left_child
                if parent.children[c_idx + 1] is None:
                    parent.children[c_idx + 1] = right_child
                    return
                else:
                    for i in range(len(parent.children) - 1, c_idx + 1, -1):
                        parent.children[i] = parent.children[i - 1]
                    parent.children[c_idx + 1] = right_child
                    # temp = right_child
                    # for i in range(c_idx + 1, len(parent.children)):
                    #     temp1 = parent.children[i]
                    #     parent.children[i] = temp
                    return

                        
            # curr.keys.append(key_p)
            
            curr.children[0] = (left_child)
            curr.children[1] = (right_child)
            return key_p
        
        return None




    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(len(node.keys)+1): 	                	
                self._print_tree(node.children[i], lvl+1)
                if i<len(node.keys):
                    print(lvl*'  ', node.keys[i])




            

    # def print_tree(self):
    #     pass




def main():
    tree = Btree(4)
    keys = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18, 15, 10, 19]
    for i in keys:
        tree.insert(i)
    tree.insert(2000)
    tree.print_tree()
    




main()