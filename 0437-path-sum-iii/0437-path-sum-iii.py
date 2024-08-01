# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''self.sum = 0
        def helper(node,cur):
            if node == None:
                return
            helper(node.left,cur+node.val)
            helper(node.right, cur+node.val)
            if cur + node.val == targetSum:
                self.sum += 1
        def dfs(node):
            if node == None:
                return
            helper(node,0)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.sum'''
        
        self.sum = 0
        d = {0:1}
        def dfs(node,cur):
            if node == None:
                return 
            ans = (cur + node.val) - targetSum
            if ans in d.keys() :
                self.sum += d[ans]
                
            d[cur+node.val] = 1 + d.get(cur+node.val,0)
            
            dfs(node.left,cur+node.val)
            dfs(node.right,cur+node.val)
            
            d[cur+node.val] -= 1
            
        dfs(root,0)
        return self.sum
            
            
            
            
            

    
    
        
        