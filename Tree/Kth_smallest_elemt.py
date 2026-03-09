# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = -1 

        def inOrder(root, k):
            nonlocal cnt, res
            if not root:
                return 

            inOrder(root.left, k)
            cnt += 1 
            if cnt == k:
                res = root.val 
                return 

            inOrder(root.right, k) 

        inOrder(root, k) 
        return res 
        