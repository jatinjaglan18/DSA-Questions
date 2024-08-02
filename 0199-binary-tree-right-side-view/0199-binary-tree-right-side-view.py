# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        arr = []
        mq = deque()
        cq = deque()
        mq.append(root)
        
        while len(mq) != 0 or len(cq) != 0:
            v = mq.popleft()
            if v.left != None:
                cq.append(v.left)
            if v.right != None:
                cq.append(v.right)
            
            if len(mq) == 0:
                arr.append(v.val)
                mq = cq
                cq = deque()
        
        return arr
        
        