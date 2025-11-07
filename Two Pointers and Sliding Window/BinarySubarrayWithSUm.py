class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            l = 0
            Sum = 0
            count = 0
            for r in range(len(nums)):
                Sum += nums[r]
                while Sum > k:
                    Sum -= nums[l]
                    l += 1
                count += (r - l + 1)
            return count

        return atMost(goal) - atMost(goal - 1)
