# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0 

        def helper(root):
            nonlocal max_diameter
            if root is None:
                return 0 
            leftNode = helper(root.left)
            rightNode = helper(root.right)
            max_diameter = max(max_diameter, leftNode+rightNode) 
            return 1 + max(leftNode, rightNode) 

        helper(root) 
        return max_diameter