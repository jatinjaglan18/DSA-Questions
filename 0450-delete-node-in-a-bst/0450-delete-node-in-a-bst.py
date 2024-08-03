# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: 
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None: 
                return root.right
            if root.right == None: 
                return root.left

            if root.left and root.right:
                temp = root.right
                while temp.left: 
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root  
                

        
        