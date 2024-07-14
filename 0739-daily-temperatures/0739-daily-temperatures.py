class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        nge = [0 for i in range(len(temperatures))]
        for i in range(1,len(temperatures)):
            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                v = stack.pop()
                nge[v] = i - v
            stack.append(i)
        
        return nge
    
            