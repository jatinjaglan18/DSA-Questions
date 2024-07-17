class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for i in range(len(matrix)):
            if matrix[i][n-1] == target:
                return True
            
            elif matrix[i][n-1] > target:
                v = self.binary_search(matrix[i],0,n-1,target)
                if v == -1:
                    return False
                else:
                    return True
                
        return False
    
    def binary_search(self,arr,l,h,x):
        '''if l<=h:
            m = h+l//2
            if arr[m] == x:
                return m
            elif arr[m] > x:
                return self.binary_search(self,arr,l,m-1,x)
                
            elif arr[m] < m:
                return self.binary_search(self,arr,m+1,h,x)
        else:
            return -1'''
        
        l = 0
        h = len(arr) - 1
        m = h+l//2
        while l <= h:
            if arr[m] == x:
                return m
            elif arr[m] < x:
                l = m+1
            elif arr[m] > x:
                h = m-1
                
            m = h+l//2
                
        else:
            return -1
                
    
            