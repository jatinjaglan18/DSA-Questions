# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        node = TreeNode(postorder.pop())
        if node.val != preorder[-1]:
            node.right = self.constructFromPrePost(preorder, postorder)

        if node.val != preorder[-1]:
            node.left = self.constructFromPrePost(preorder, postorder)
        
        preorder.pop()

        return node
