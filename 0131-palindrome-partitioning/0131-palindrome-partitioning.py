class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        def partitions(s):
            if len(s) == 1 :
                return [[s]]
            
            ch = s[0]
            ans = partitions(s[1:])
            res = []
           
            for i in ans:
                res.append([ch] + i)
                res.append([ch + i[0]]+i[1:])
            
            return res
        
        p = partitions(s)
        
        def palindrome(s):
            if len(s) == 1:
                return True
            return s == s[::-1]
            
        result = []
        for i in p:
            for j in i:
                if not palindrome(j):
                    break
            else:
                result.append(i)
                
        return result
                
    
    
            
            