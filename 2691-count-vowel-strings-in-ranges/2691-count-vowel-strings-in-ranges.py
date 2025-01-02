class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowles = ['a','e','i','o','u']

        '''ans = []
        for s, e in queries:
            count = 0
            for i in range(s,e+1):
                s = words[i]
                if s[0] in vowles and s[-1] in vowles:
                    count += 1
            ans.append(count)
        return ans'''
        ans = []
        dp = [0]*len(words)
        if words[0][0] in vowles and words[0][-1] in vowles:
                dp[0] = 1
        for i in range(1,len(words)):
            word = words[i]
            if word[0] in vowles and word[-1] in vowles:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        for s,e in queries:
            if s == 0:
                ans.append(dp[e])
            elif s==e:
                if words[s][0] in vowles and words[s][-1] in vowles:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                ans.append(dp[e]-dp[s-1])
        return ans




