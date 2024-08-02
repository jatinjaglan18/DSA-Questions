# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = root.val
        level_sum = 0
        level = 1
        res = 1
        mq = deque()
        cq = deque()
        mq.append(root)
        while len(mq) != 0 or len(cq) != 0:
            v = mq.popleft()
            level_sum += v.val
            
            if v.left != None:
                cq.append(v.left)
            if v.right != None:
                cq.append(v.right)
                
            if len(mq) == 0:
                mq = cq
                cq = deque()
                
                if level_sum > max_sum:
                    max_sum = level_sum
                    res = level
                    
                level += 1
                level_sum = 0
                
        return res
                    
                    
            
            
        
                