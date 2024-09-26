# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = root.val
        if not root:
            return 0
        
        def DFS(root):
            if not root:
                return 0
            
            left_path_sum = max(DFS(root.left), 0)
            right_path_sum = max(DFS(root.right), 0)

            self.max_path_sum = max(self.max_path_sum, left_path_sum + right_path_sum + root.val)

            return max(left_path_sum, right_path_sum) + root.val

        DFS(root)
        return self.max_path_sum
            
            