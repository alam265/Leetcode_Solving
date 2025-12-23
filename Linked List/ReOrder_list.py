# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        p2 = slow.next 
        slow.next = None
        prev = None 
        
        while p2: 
            temp = p2.next 
            p2.next = prev 
            prev = p2 
            p2 = temp 


        p1, p2 = head, prev 

        while p2: 
            temp1 = p1.next 
            temp2 = p2.next 

            p1.next = p2 
            p2.next = temp1 
            
            p1 = temp1
            p2 = temp2 









