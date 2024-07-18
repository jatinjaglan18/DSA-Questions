class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.merge(nums1,nums2)
        mid = len(nums) // 2
        if len(nums) % 2 == 0: 
            median = (nums[mid-1] + nums[mid]) / 2
            return median
        else:
            return (nums[mid])
        
    
    def merge(self,arr1,arr2):
        a1 = 0
        a2 = 0
        arr = []
        while a1 < len(arr1) and a2 < len(arr2):
            if arr1[a1] < arr2[a2]:
                arr.append(arr1[a1])
                a1 += 1
            else:
                arr.append(arr2[a2])
                a2 += 1
        
        while a1 < len(arr1):
            arr.append(arr1[a1])
            a1 += 1
        
        while a2 < len(arr2):
            arr.append(arr2[a2])
            a2 += 1
    
        return arr