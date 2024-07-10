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
        
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            if fast == None or fast.next == None:
                slow.next = slow.next.next
                
            else:  
                slow = slow.next
            
        return head
        