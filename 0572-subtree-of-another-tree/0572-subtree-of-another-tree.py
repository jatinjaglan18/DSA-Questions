# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        if root == None:
            return False
        if self.isSame(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
        
    def isSame(self,p,q):
        if p == None and q == None:
            return True
        if p != None and q!= None and p.val == q.val:
            l = self.isSame(p.left,q.left)
            r = self.isSame(p.right,q.right)
                
            return (l and r)
            
                