class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        s = 0
        odd = 0
        even = 0
        ans = 0

        for i in arr:
            s += i

            if s % 2 == 1:
                odd+=1
                ans += even + 1
            else:
                even += 1
                ans += odd

        mod = (10 ** 9) + 7
        return ans % mod