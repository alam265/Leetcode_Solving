# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head 
        length = 0 
        
        while p:
            length+=1 
            p = p.next 

        if length == n: 
            newHead = head.next 
            head.next = None 
            head = newHead 

        else: 
            itr = length - n - 1 
            p1 = head 
            for i in range(itr): 
                p1 = p1.next 

            p1.next = p1.next.next 

        return head













