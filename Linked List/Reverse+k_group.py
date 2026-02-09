# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head 
        cnt = 0 

        while cnt < k:
            if curr == None:
                return head
            curr = curr.next 
            cnt+=1

        prevNode = self.reverseKGroup(curr, k) 

        curr = head 
        cnt = 0 
        

        while cnt < k: 
            nextNode = curr.next
            curr.next = prevNode 
            prevNode = curr 
            curr = nextNode
            cnt += 1

        return prevNode
    

"""

Solution by Apna college


"""