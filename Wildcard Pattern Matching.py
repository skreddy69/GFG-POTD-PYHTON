class Solution:
    def wildCard(self, pattern, string):
        m, n = len(pattern), len(string)
        # Initialize the DP table with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches with empty string
        dp[0][0] = True
        
        # Handle patterns like "*", "**", "***", etc.
        for i in range(1, m + 1):
            if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == '*':
                    # '*' can either match no character (dp[i-1][j]) or match one more character (dp[i][j-1])
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif pattern[i - 1] == '?' or pattern[i - 1] == string[j - 1]:
                    # '?' matches any single character, so check the previous state
                    dp[i][j] = dp[i - 1][j - 1]
        
        # The answer is whether the entire pattern matches the entire string
        return dp[m][n]



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends