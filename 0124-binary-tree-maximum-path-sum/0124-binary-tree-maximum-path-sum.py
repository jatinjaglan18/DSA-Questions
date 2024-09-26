# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        if root == None:
            return 0
        
        def DFS(root):
            if root == None:
                return 0
            
            l = max(DFS(root.left), 0)
            r = max(DFS(root.right), 0)

            self.max_sum = max(self.max_sum, l + r + root.val)

            return max(l, r) + root.val

        DFS(root)
        return self.max_sum
            
            