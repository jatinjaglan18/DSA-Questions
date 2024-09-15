# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''if root == None:
            ht = 0
            return ht
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        ht = max(l,r) + 1
        
        return ht'''
        if root == None:
            return 0
        q = [root]
        cq = []
        count = 0
        while len(q) != 0 or len(cq) != 0:
            val = q.pop(0)
            
            if val.left != None:
                cq.append(val.left)
            if val.right != None:
                cq.append(val.right)
            
            if len(q) == 0:
                q = cq
                cq = []
                count += 1
            
        return count
        