# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        arr = []
        mq = [root]
        cq = []
        
        while len(mq) != 0 or len(cq) != 0:
            v = mq.pop(0)
            if v.left != None:
                cq.append(v.left)
            if v.right != None:
                cq.append(v.right)
            
            if len(mq) == 0:
                arr.append(v.val)
                mq = cq
                cq = []
        
    
        return arr
        
        