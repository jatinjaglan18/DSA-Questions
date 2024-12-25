# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        cq = []
        level = []
        res = [root.val]

        while q:
            v = q.pop()
            if v.left:
                level.append(v.left.val)
                cq.append(v.left)
            if v.right:
                level.append(v.right.val)
                cq.append(v.right)
            
            if len(q) == 0:
                if level:
                    m = max(level)
                    res.append(m)
                q=cq
                cq = []
                level = []
        return res