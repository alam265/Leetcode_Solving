# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True 
        
        def helper(root):
            nonlocal isBalanced
            if root is None:
                return 0 
            left = helper(root.left)
            right = helper(root.right) 

            if abs(right - left) > 1:
                isBalanced = False
            
            return 1 + max(left, right) 
        
        helper(root) 
        return isBalanced