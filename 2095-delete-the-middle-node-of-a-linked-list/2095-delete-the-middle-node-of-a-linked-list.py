# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        elif head.next.next == None:
            head.next = None
            return head
        
        p1 = head
        p2 = head
        
        while p2 != None and p2.next != None:
            p2 = p2.next.next
            if p2 == None or p2.next == None:
                p1.next = p1.next.next
            p1 = p1.next
                
        return head
        