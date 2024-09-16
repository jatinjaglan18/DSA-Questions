# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def daimeter(node):
            
            if node == None:
                arr = [-1,0]
                return arr
        
            l = daimeter(node.left)
            r = daimeter(node.right)
            
            ht = max(l[0], r[0]) + 1
            c_d = l[0] + r[0] + 2
            dai = max(c_d, l[1], r[1])
            
            return [ht,dai]
         
        return(daimeter(root)[1])
        
        
     
        