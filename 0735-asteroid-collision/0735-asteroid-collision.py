class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in asteroids:
            if len(stack) != 0 and i < 0 and stack[-1] > 0:
                while stack[-1] > 0 and abs(i) >= stack[-1]:
                    if abs(i) == stack[-1] :
                        stack.pop()
                        break
                    stack.pop()
    
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(i)
            else:
                stack.append(i)
        return stack
            
            
            
        