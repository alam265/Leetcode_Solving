# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, leftVal, rightVal):
            if not root:
                return True 
            if leftVal < root.val < rightVal:
                return valid(root.left, leftVal, root.val) and valid(root.right, root.val, rightVal) 

            else: 
                return False 


        return valid(root, float("-inf"), float("inf")) 
