class Solution:
    def minimumLength(self, s: str) -> int:
        count = 0
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1
        
        for i in freq.values():
            if i <= 2:
                count += i
            elif i % 2 == 0:
                count += 2
            else:
                count += 1

        return count