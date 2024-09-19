# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.subroot = TreeNode()
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p,q):
            if p == None and q == None:
                return True
            if p != None and q!= None and p.val == q.val:
                l = isSame(p.left,q.left)
                r = isSame(p.right,q.right)
                
                return (l and r)
            
        if root == None:
            return False
        if isSame(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
        
                