class Elem:
    def __init__(self,priority,data) -> None:
        
        self.__data = data
        self.__priority = priority
    
    def __lt__(self,other):
        return self.__priority < other.__priority

    def __gt__(self,other):
        return self.__priority > other.__priority
    
    def __repr__(self):
        return (f"{self.__priority} : {self.__data}")

class Selsort:
    def swap(tab):

        pass
    def shift(tab):
        pass

def main():
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]    
    tab = [ Elem(key, value) for key,value in  data]
    
