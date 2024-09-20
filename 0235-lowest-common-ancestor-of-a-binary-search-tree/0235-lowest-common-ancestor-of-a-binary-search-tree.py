# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        
        
        
        
        
        
        '''p_root = self.node_to_root(root,p)
        q_root = self.node_to_root(root,q)
        
        i = len(p_root) - 1
        j = len(q_root) - 1
        
        while i >= 0 and j >= 0 and p_root[i].val == q_root[j].val:
            i -= 1
            j -= 1
        return p_root[i+1]
        
    def node_to_root(self,root,node):
        if root == None:
            return []
        
        if node.val < root.val:
            arr = self.node_to_root(root.left,node)
            arr.append(root)
            return arr
        elif node.val > root.val:
            arr = self.node_to_root(root.right,node)
            arr.append(root)
            return arr
        else:
            return [node]'''
        
        
        
    