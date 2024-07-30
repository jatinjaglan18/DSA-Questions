# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def node_to_root(node,x):
    if node == None:
        return []
    if node == x:
        arr = [node]
        return arr
    l = node_to_root(node.left,x)
    if len(l) != 0:
        l.append(node)
        return l
    r = node_to_root(node.right,x)
    if len(r) != 0:
        r.append(node)
        return r
    
    return []
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = node_to_root(root,p)
        b = node_to_root(root,q)
        i = len(a)-1
        j = len(b)-1
        
        while a[i] == b[j]:
            i -= 1
            j -= 1
        
        i += 1
        j += 1
       
        return a[i]
        
            
        
        