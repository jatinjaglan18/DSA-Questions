# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for i in range(k):
            if temp == None:
                return head     
            temp = temp.next
        
        prev = None
        temp = head
        for i in range(k):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            
        head.next = self.reverseKGroup(temp,k)
        return prev
            