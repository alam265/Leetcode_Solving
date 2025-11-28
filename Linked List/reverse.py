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