# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = collections.deque() 
        q.append(root) 
        rightView = None
        res = [] 

        while q: 
            for _ in range(len(q)): 
                node = q.popleft() 
                rightView = node 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 

            res.append(rightView.val) 

        return res 
