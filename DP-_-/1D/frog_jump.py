class Solution:
    def frogJump(self, height):
        n = len(height)

        if n == 1:
            return 0

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):

            fs = dp[i-1] + abs(height[i] - height[i-1])

            ss = float('inf')
            if i > 1:
                ss = dp[i-2] + abs(height[i] - height[i-2])

            dp[i] = min(fs, ss)

        return dp[n-1]
