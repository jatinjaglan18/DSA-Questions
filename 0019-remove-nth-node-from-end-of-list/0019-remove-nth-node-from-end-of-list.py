# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        temp = head
        temp1 = head
        size = 0
        while temp != None:
            size += 1
            temp = temp.next
        
        
        r = size- n
        if r == 0:
            return head.next
        idx = 0 
        while temp1 != None:
            idx += 1
            if idx == size - 1:
                temp1.next = None
                return head
                
            elif idx == r:
                temp1.next = temp1.next.next
                return head
            temp1 = temp1.next
        
        
        
            