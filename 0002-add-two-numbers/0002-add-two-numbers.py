# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        temp = l
        c = 0
        temp1 = l1
        temp2 = l2
        
        while temp1 != None and temp2 != None:
            val = temp1.val+temp2.val+c
            c = val // 10
            val = val % 10
            
            
            new = ListNode(val)

            temp.next = new
            temp = new
            
            temp1 = temp1.next
            temp2 = temp2.next
            
        while temp1 != None:
            val = temp1.val+c
            c = val // 10
            val = val % 10
            
            
            new = ListNode(val)
            temp.next = new
            temp = new
            temp1 = temp1.next
                
        while temp2 != None:
            val = temp2.val+c
            c = val // 10
            val = val % 10
            
            
            new = ListNode(val)
            temp.next = new
            temp = new
            temp2 = temp2.next
            
            
            
        if c != 0:
            new = ListNode(1)
            temp.next = new
            temp = new
            
        
        return l.next
            
            
        
        
        
        
            
        
        