# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = [root]
        cq = []
        res = []
        child = []
        while q:
            val = q.pop(0)
            child.append(val.val)
            
            if val.left != None:
                cq.append(val.left)
            if val.right != None:
                cq.append(val.right)
                
            if len(q) == 0:
                q = cq
                cq = []
                res.append(child)
                child = []
        return res