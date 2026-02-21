# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0 
        maxVal = float("-inf")

        def helper(root, maxVal):
            nonlocal cnt
            if not root:
                return 
            if root.val >= maxVal:
                cnt += 1
                maxVal = root.val 

            helper(root.left, maxVal) 
            helper(root.right, maxVal) 

        helper(root, maxVal) 
        return cnt