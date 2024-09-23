# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isbinary(node):
            if node == None:
                return (True, float('inf'), float('-inf'))   #isbst,  minimum,  maximum

            lbst, lmin, lmax  = isbinary(node.left)
            rbst, rmin, rmax = isbinary(node.right)
    

            nmin = min(node.val,lmin,rmin)
            nmax = max(node.val,lmax,rmax)

            if lbst and rbst and node.val > lmax and node.val < rmin:
                return (True , nmin, nmax)
            else:
                return (False, nmin, nmax)

        return isbinary(root)[0]

            