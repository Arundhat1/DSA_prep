#recursion + memoization
class Solution:
    def ninjaTraining(self, n, points):

        dp = [[-1]*4 for _ in range(n)]

        def solve(day, last):

            if day == 0:
                maxi = 0
                for task in range(3):
                    if task != last:
                        maxi = max(maxi, points[0][task])
                return maxi

            if dp[day][last] != -1:
                return dp[day][last]

            maxi = 0

            for task in range(3):
                if task != last:
                    val = points[day][task] + solve(day-1, task)
                    maxi = max(maxi, val)

            dp[day][last] = maxi
            return maxi

        return solve(n-1, 3)
# tabulation
class Solution:
    def ninjaTraining(self, n, points):

        dp = [[0]*4 for _ in range(n)]

        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0])

        for day in range(1, n):
            for last in range(4):

                dp[day][last] = 0

                for task in range(3):

                    if task != last:
                        activity = points[day][task] + dp[day-1][task]
                        dp[day][last] = max(dp[day][last], activity)

        return dp[n-1][3]
