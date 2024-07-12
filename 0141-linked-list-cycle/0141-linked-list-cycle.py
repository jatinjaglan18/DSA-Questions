# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        while head != None:
            if head in d.keys():
                return True
            else:
                d[head] = head
            head = head.next
        else:
            return False