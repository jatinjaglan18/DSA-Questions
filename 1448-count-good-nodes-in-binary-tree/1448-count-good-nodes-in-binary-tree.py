# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def good(node,high):
    if node == None:
        return 0
    high = max(high, node.val)
    l = good(node.left,high)
    r = good(node.right,high)
    
    if high <= node.val:
        return 1 + l + r
    else:
        return l + r
        
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return good(root,float('-inf'))

        
            
        
        
        