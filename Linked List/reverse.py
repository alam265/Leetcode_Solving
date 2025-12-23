class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head 
        q = None 
        r = None 

        while p: 
            r = q 
            q = p 
            p = p.next 
            q.next = r  

        return q
    

"""Using 2 pointers"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head 
        prev = None 
        while p: 
            temp = p.next 
            p.next = prev 
            prev = p 
            p = temp 
        return prev