class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.merge(nums1,nums2)
        print(nums)
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (nums[-1] + nums[-2]) / 2
        else:
            return nums[-1]
    
    def merge(self,arr1,arr2):
        a1 = 0
        a2 = 0
        mid = ((len(arr1) + len(arr2)) // 2)+1
        arr = []
        while a1 < len(arr1) and a2 < len(arr2):
            if len(arr) == mid:
                return arr
            if arr1[a1] < arr2[a2]:
                arr.append(arr1[a1])
                a1 += 1
            else:
                arr.append(arr2[a2])
                a2 += 1
        
        while a1 < len(arr1):
            if len(arr) == mid:
                return arr
            arr.append(arr1[a1])
            a1 += 1
        
        while a2 < len(arr2):
            if len(arr) == mid:
                return arr
            arr.append(arr2[a2])
            a2 += 1
            
        return arr
    
        