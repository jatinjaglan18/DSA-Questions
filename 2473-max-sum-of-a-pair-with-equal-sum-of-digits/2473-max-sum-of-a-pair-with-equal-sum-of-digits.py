class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        ans = -1
        for num in nums:
            curr = sum(int(digit) for digit in str(num)) # get sum of digits
            if curr in dic:
                ans = max(ans, num + dic[curr])
                dic[curr] = max(dic[curr], num)
            else:
                dic[curr] = num
        return ans