# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = collections.deque()
        q.append(root)
        res = [] 

        while q: 
            lst = [] 
            for _ in range(len(q)): 
                node = q.popleft() 
                lst.append(node.val) 

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 

            if lst: 
                res.append(lst)  

        return res



