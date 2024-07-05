class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l != r:
            width = r-l
            
            if height[l] < height[r]:
                high = height[l]
                l += 1
            else:
                high = height[r]
                r -= 1
                
            area = width * high
            if area > max_area:
                max_area = area
        
        return max_area
                
            
            
        
                
                