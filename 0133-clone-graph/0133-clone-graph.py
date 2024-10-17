"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return node
        q = [node]
        cloned = {node.val : Node(node.val)}
        
        while q:
            cur = q.pop(0)
            cur_clone = cloned[cur.val]
            
            for nbr in cur.neighbors:
                if nbr.val not in cloned:
                    cloned[nbr.val] = Node(nbr.val)
                    q.append(nbr)
                cur_clone.neighbors.append(cloned[nbr.val])
                
        return cloned[node.val]