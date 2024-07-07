class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        '''l = []
        for i in n1:
            if i in n2:
                n2.remove(i)
            else:
                l.append(i)
        
        ans=[[],[]]
        ans[0] = l
        ans[1] = n2
        
        return ans'''
                
        l1 = list(n1-n2)
        l2 = list(n2-n1)
        
        ans = [l1,l2]
        return ans