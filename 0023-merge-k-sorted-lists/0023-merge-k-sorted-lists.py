# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            
            temp = []
            
            for i in range(0,len(lists),2):
                
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                
                temp.append(self.merge(l1,l2))
                
            lists = temp
        
        return lists[0]
        
    def merge(self,l1,l2):
        l = ListNode()
        temp = l
        temp1 = l1
        temp2 = l2
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp = temp.next
                temp2 = temp2.next
                
        while temp1:
            temp.next = temp1
            temp = temp.next
            temp1 = temp1.next
            
        while temp2:
            temp.next = temp2
            temp = temp.next
            temp2 = temp2.next
            
        return l.next
                
            
            
            
            
        
        
                    
            