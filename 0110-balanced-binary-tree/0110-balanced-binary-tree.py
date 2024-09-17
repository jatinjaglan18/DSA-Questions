# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def isbal(node):
            if node == None:
                return -1
            lh = isbal(node.left)
            rh = isbal(node.right)

            ht = max(lh,rh) + 1
            if abs(lh-rh) > 1:
                self.flag = False

            return ht
        isbal(root)
        
        return self.flag