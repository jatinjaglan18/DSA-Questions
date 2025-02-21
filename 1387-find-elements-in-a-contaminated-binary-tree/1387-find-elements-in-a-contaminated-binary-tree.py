# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def dfs(self, root):
        if root == None:
            return
        if root.left != None:
            root.left.val = (2 * root.val) + 1
            self.s.add(root.left.val)
        self.dfs(root.left)
        if root.right != None:
            root.right.val = (2 * root.val) + 2
            self.s.add(root.right.val)
        self.dfs(root.right)

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.s = set()
        self.s.add(0)
        self.dfs(root)
        
    def find(self, target: int) -> bool:
        if target in self.s:
            return True
        else:
            return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)