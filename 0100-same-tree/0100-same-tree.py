# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if p != None and q != None and p.val==q.val:
            l = self.isSameTree(p.left,q.left)
            r = self.isSameTree(p.right,q.right)
            
            return l and r
        
        return False