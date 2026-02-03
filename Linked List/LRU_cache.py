class Node:
    def __init__(self, key, val): 
        self.key = key 
        self.val = val 
        self.next = self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} 
        self.left , self.right = Node(0,0), Node(0,0)
        self.left.next = self.right 
        self.right.prev = self.left

    def remove(self, node): 
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert(self, node):
        prevNode, nextNode = self.right.prev, self.right
        prevNode.next = node 
        nextNode.prev = node 
        node.prev = prevNode 
        node.next = nextNode
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val  
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        
