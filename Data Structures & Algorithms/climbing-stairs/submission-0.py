class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] + [1] + [-1] * (n-1)
        for l in range(2,n+1):
            dp[l] = dp[l-1] + dp[l-2]
        return dp[n]