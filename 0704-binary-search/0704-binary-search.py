class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #return self.binary_search(nums,0,len(nums)-1,target)
        l = 0
        h = len(nums) - 1
        m = h+l//2
        while l <= h:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m-1
            elif nums[m] < target:
                l = m+1
                
            m = h+l//2
        
        else:
            return -1
            
    '''def binary_search(self,arr,l,h,x):
        if h >= l:
            m = (h + l) // 2
            if arr[m] == x:
                return m
            elif arr[m] > x:
                return self.binary_search(arr,l,m-1,x)

            elif arr[m] < x:
                return self.binary_search(arr,m+1,h,x)
            
            
        else:
            return -1'''
       