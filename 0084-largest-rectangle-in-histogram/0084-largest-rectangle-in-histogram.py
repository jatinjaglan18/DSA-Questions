class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lb = [-1] * len(heights)
        rb = [len(heights)]*len(heights)
        stack = []
        stack.append(len(heights) - 1)
        for i in range(len(heights)-2,-1,-1):
            while heights[i] <= heights[stack[-1]]:
                stack.pop()
                if len(stack) == 0:
                    rb[i] = len(heights)
                    stack.append(i)
                    break
            else:
                rb[i] = stack[-1]
                stack.append(i)
                
            
        stack = []
        stack.append(0)
        for i in range(1,len(heights)):
            while heights[i] <= heights[stack[-1]]:
                stack.pop()
                if len(stack) == 0:
                    lb[i] = -1
                    stack.append(i)
                    break
            else:
                lb[i] = stack[-1]
                stack.append(i)
                
        print(lb)
        print(rb)
        max_area = 0
        for i in range(len(heights)):
            high = heights[i]
            width = rb[i] - lb[i] - 1
            area = high*width
            if area > max_area:
                max_area = area
        return max_area
    
    
            
            
            
            
        
        
            
            
        
        