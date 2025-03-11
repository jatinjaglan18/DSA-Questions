class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {}
        left = ans = 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)

            while all(freq.get(ch,0) > 0 for ch in 'abc'):
                ans += len(s) - right
                freq[s[left]] -= 1
                left += 1
        
        return ans