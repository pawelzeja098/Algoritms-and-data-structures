class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self) -> None:
        self.head = None
    
    def insert_node(self,data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def destroy(self) -> None:
        self.head = None

    def add(self,data) -> None:
        pass

    def append(self,data) -> None:
        pass

    def remove(self) -> None:
        pass

    def remove_end(self) -> None:
        pass

    








def main():
    uczelnie = [('AGH', 'Kraków', 1919),
               ('UJ', 'Kraków', 1364),
               ('PW', 'Warszawa', 1915),
               ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919),
               ('PG', 'Gdańsk', 1945)]
    