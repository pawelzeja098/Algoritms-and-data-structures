class Node:
    #create the linked list
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class Linked_list:
    
    #transformators
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    #add to the beggining of the list
    def add(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    #add to the end of the list
    def append(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    #remove from beggining of the list
    def remove(self) -> None:
        if self.head is None:
            print("Can't remove from an empty list")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    #remove from the end of the list
    def remove_end(self) -> None:
        if self.head is None:
            print("Can't remove from an empty list")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
 
    def display(self, quantity):
        current_node = self.head
        res = ''
        i = 0
        while(i < quantity):
        
            res += str(current_node.data) + '\n'
            current_node = current_node.next
            i += 1
        print(res)

         
   
    #destroy the list
    def destroy(self) -> None:
        current_node = self.head
        while current_node:
            next_node = current_node.next
            del current_node
            current_node = next_node
        self.head = None
        self.tail = None

    

    #observators
    def is_empty(self) -> bool:
        if self.head is None:
            return True
        return False

    def length(self) -> int:
        if self.head is None:
            return 0
        current_node = self.head
        length = 0
        while(current_node):
            current_node = current_node.next
            length += 1
        return length
            
    
    def get(self):
        return self.head.data


def main():
    data = [('AGH', 'Kraków', 1919),
               ('UJ', 'Kraków', 1364),
               ('PW', 'Warszawa', 1915),
               ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919),
               ('PG', 'Gdańsk', 1945)]
    uczelnie = Linked_list()
    
    for i in data[:3]:
        uczelnie.append(i)
    for i in data[3:]:
        uczelnie.add(i)
    uczelnie.display(uczelnie.length())
    print(uczelnie.length())
    uczelnie.remove()
    uczelnie.display(1)
    uczelnie.remove_end()
    uczelnie.display(uczelnie.length())
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(data[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

main()