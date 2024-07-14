class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        d = {}
        for i in range(len(speed)):
            d[position[i]] = speed[i]
        
        
        l = list(sorted(d.keys()))
        for i in range(len(l)-1,-1,-1):
            des_t = (target - l[i]) / d[l[i]]
            
            if len(stack) == 0 or stack[-1] < des_t:
                stack.append(des_t)
                
                
        return len(stack)
            
        
        
        
        