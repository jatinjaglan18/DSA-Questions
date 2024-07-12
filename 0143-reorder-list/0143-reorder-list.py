# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.head = head
        self.temp = head
        self.m = self.mid(head)
        self.helper(self.temp,0)
        
    def mid(self,head):
        idx = 0
        s = head
        f = head
        
        while f != None and f.next != None:
            idx += 1
            s = s.next
            f = f.next.next
        return idx
        
    def helper(self,temp,i):
        if temp == None:
            return
        self.helper(temp.next,i+1)
        if i == self.m:
            temp.next = None
            return
        elif i < self.m:
            return
            
        temp.next = self.head.next
        self.head.next = temp
        self.head = self.head.next.next
        