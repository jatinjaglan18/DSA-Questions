# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        cq = []
        ans = []
        while q:
            val = q.pop(0)
            if val.left:
                cq.append(val.left)
            if val.right:
                cq.append(val.right)
            
            if len(q) == 0:
                ans.append(val.val)
                q = cq
                cq = []
                
 
        return ans