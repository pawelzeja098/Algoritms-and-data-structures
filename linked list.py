class Node:
    #create the listed list
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linked_list:
    
    #transformators
    
    def __init__(self) -> None:
        self.head = None
    
    #add to the beggining of the list
    def add(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    #add to the end of the list
    def append(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            
            current_node.next = new_node


    #remove from beggining of the list
    def remove(self) -> None:
        if self.head is None:
            raise TypeError("Can`t remove from an empty list")
        self.head = self.head.next

    #remove from the end of the list
    def remove_end(self) -> None:
        if self.head is None:
            raise TypeError("Can`t remove from an empty list")
        current_node = self.head
        while(current_node.next.next is not None):
            current_node = current_node.next
        current_node.next.next = None
 
    def display(self):
        while 
   
    #destroy the list
    def destroy(self) -> None:
        self.head = None

    #observators
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def length(self):
        if self.head is None:
            return 0
        current_node = self.head
        length = 0
        while(current_node.next is not None):
            current_node = current_node.next
            length += 1
        return length
            
    
    def get(self):
        return self.head


def main():
    uczelnie = [('AGH', 'Kraków', 1919),
               ('UJ', 'Kraków', 1364),
               ('PW', 'Warszawa', 1915),
               ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919),
               ('PG', 'Gdańsk', 1945)]
    