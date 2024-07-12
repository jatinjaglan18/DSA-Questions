"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        ref = {}
        temp = head
        while temp :
            ref[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp != None:
            if temp.next:
                ref[temp].next = ref[temp.next]
            if temp.random:
                ref[temp].random = ref[temp.random]
            temp = temp.next
        
        
        return ref[head]