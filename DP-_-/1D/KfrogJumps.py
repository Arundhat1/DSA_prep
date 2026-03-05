class Solution:

    def solveUtil(self, n, height, dp, k):
      if not height:
        return
      dp = [float('inf')]
      dp[0] = 0
      for i in range(1,n):
        mmSteps = float('inf')
        for j in range(1,k+1):
          if i - j >= 0:
            jump = dp[i-j] + abs(height[i] - height[i-j])
            mmSteps = min(jump,mmSteps)
        dp[i] = mmSteps
      return dp[-1]  
