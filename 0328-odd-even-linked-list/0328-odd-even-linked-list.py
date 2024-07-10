# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        
        odd_ptr = odd
        even_ptr = even
        
        idx = 1
        while head != None:
            new = ListNode(head.val)
            if idx % 2 != 0:
                odd_ptr.next = new
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = new
                even_ptr = even_ptr.next
            head = head.next
            idx += 1
        
        odd_ptr.next = even.next
        
        return odd.next
                
        
        
       
            
        