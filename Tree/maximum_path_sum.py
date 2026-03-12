# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf") 

        def helper(root):
            nonlocal maxPath
            if not root:
                return 0 

            left = helper(root.left) 
            right = helper(root.right) 
            leftMax = max(left, 0) 
            rightMax = max(right, 0)

            maxPath = max(maxPath, leftMax + rightMax + root.val) 

            return root.val + max(leftMax, rightMax)

        helper(root)

        return maxPath
        