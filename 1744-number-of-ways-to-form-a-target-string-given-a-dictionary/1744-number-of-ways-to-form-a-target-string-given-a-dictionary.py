class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        m, n = len(words[0]), len(target)

        # Step 1: Precompute character frequencies in each column
        freq = [[0] * 26 for _ in range(m)]
        for word in words:
            for i in range(m):
                freq[i][ord(word[i]) - ord('a')] += 1

        # Step 2: Dynamic Programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(n + 1):
                # Case 1: Skip the current column
                dp[i][j] = dp[i - 1][j]

                # Case 2: Use the current column (only if j > 0)
                if j > 0:
                    char_index = ord(target[j - 1]) - ord('a')
                    dp[i][j] += dp[i - 1][j - 1] * freq[i - 1][char_index]
                    dp[i][j] %= MOD

        return dp[m][n]
