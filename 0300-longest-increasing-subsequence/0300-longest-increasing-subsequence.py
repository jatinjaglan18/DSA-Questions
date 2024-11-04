import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        
        '''def binarySearch(res, n):
            left = 0
            right = len(res) - 1
            
            while left <= right :
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
                
            return left'''
        
        for i in nums:
            if len(res) == 0 or res[-1] < i:
                res.append(i)
            else:
                '''idx = binarySearch(res,i)
                res[idx] = i'''
                
                res[bisect.bisect_left(res,i)] = i
        
        return len(res)
                    