class Solution:
    def minOperations(self, str1: str, str2: str) -> int:
        n = len(str1)
        m = len(str2)

        # Create a 2D DP array
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP array to compute LCS length
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Length of LCS
        lcs_length = dp[n][m]

        # Calculate the minimum deletions and insertions
        min_deletions = n - lcs_length
        min_insertions = m - lcs_length

        # Return total operations
        return min_deletions + min_insertions

