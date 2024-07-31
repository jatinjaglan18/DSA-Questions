# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.m = float('-inf')
        def zigzag(node,left,right):
            self.m = max(self.m,left,right)
            
            if node.left:
                zigzag(node.left,right+1,0)
            if node.right:
                zigzag(node.right,0,left+1)
                
        zigzag(root,0,0)
        return self.m
            
                
        
        