class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def extend_around_center(s,left,right):
            count = 0 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    count+=1
                    left -= 1
                    right += 1 
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += extend_around_center(s,i,i)
            ans += extend_around_center(s,i,i+1)
            
        return ans
        