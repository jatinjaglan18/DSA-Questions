# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


    
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        r1 = self.leaf(root1)
        r2 = self.leaf(root2)
    
        return r1 == r2
    def leaf(self,node):
        if node == None:
            return []
        if node.left == None and node.right == None:
            arr = []
            arr.append(node.val)
            return arr
        
        l = self.leaf(node.left)
        r = self.leaf(node.right)
        return l + r
        
        
        