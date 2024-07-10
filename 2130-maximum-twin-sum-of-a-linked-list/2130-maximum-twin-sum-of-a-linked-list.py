# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head
        stack = []
        s = 0
        
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        while len(stack) > 0 and slow != None:
            p = stack.pop()
            v = slow.val + p
            if s < v:
                s = v
            slow = slow.next
        return s
       
            
            
            
            
    