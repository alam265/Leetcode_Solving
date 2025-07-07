class Node: 
    def __init__(self,key,val): 
        self.key = key 
        self.value = val
        self.next = None 

class MyHashMap:

    def __init__(self):
        self.map = [None]*10**4
        

    def put(self, key: int, value: int) -> None: 
        idx = key%len(self.map)
        if self.map[idx] is None: 
            self.map[idx] = Node(key, value) 

        else: 
            curr = self.map[idx] 
            while curr: 
                if curr.key == key: 
                    curr.value = value 
                    return 
                
                if curr.next is None: 
                    break 
                curr = curr.next 
            curr.next = Node(key, value)


        

    def get(self, key: int) -> int:
        idx = key % len(self.map) 
        curr = self.map[idx] 

        while curr: 
            if curr.key == key: 
                return curr.value 
            curr = curr.next 
        return -1 
            
        

    def remove(self, key: int) -> None:
        idx = key % len(self.map) 
        curr = self.map[idx] 
        prev = None  

        while curr: 
            if curr.key == key: 
                if prev is None: 
                    self.map[idx] = curr.next 
                else: 
                    prev.next = curr.next 
            prev = curr 
            curr = curr.next 
            
