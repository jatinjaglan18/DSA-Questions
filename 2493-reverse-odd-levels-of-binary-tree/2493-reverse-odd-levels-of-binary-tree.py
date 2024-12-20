# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        cq = []
        rev = True
        while q:
            node = q.pop(0)
            if node.left:
                cq.append(node.left)
            if node.right:
                cq.append(node.right)
            if len(q) == 0:
                if rev:
                    for i in range(len(cq) // 2):
                        cq[i].val, cq[-i-1].val = cq[-i-1].val, cq[i].val
                q = cq
                cq = []
                rev = not rev
        return root