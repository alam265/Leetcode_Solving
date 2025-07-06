class Node: 
    def __init__(self, key):
        self.key = key 
        self.next = None 


class MyHashSet:

    def __init__(self):
        self.set = [None] * 10**4

    def add(self, key: int) -> None:
        idx = key % len(self.set)
        if self.set[idx] is None:
            self.set[idx] = Node(key)
            return

        curr = self.set[idx]
        while curr:
            if curr.key == key:
                return  # Key already exists
            if curr.next is None:
                break
            curr = curr.next
        # Only insert if we reached end without finding the key
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.set)
        curr = self.set[idx]
        prev = None
        while curr:
            if curr.key == key:
                if prev is None:
                    self.set[idx] = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        idx = key % len(self.set)
        curr = self.set[idx]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)