# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""Naive Approach"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        curr1 = head 
        curr2 = head 

        nextNode = None 
        prevNode = None 

        for i in range(left-1):
            nextNode = curr1 
            curr1 = curr1.next 

        for j in range(right-1):
            curr2 = curr2.next 

        prevNode = curr2.next 
        curr = curr1
        for k in range(right- left + 1):
            temp = curr.next
            curr.next = prevNode 
            prevNode = curr
            curr = temp 

        if nextNode:
            nextNode.next = prevNode 
        else:
            head = prevNode

        return head
    



"""Optimal - one pass"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev = dummy 
        curr = head 
        for i in range(left-1):
            leftPrev = curr 
            curr = curr.next 

        prev = None 
        for j in range(right-left+1):
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        leftPrev.next.next = curr 
        leftPrev.next = prev 
        

        return dummy.next