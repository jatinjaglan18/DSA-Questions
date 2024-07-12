# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        l = ListNode()
        temp3 = l
        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val:
                temp3.next = temp1
                temp3 = temp3.next
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp3 = temp3.next
                temp2 = temp2.next

        while temp1 != None:
            temp3.next = temp1
            temp3 = temp3.next
            temp1 = temp1.next

        while temp2 != None:
            temp3.next = temp2
            temp3 = temp3.next
            temp2 = temp2.next
            
        return l.next