class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(goal):
            if goal <0:
                return 0
            n = len(nums)
            res = 0
            
            l,r = 0,0
            count = {}
            while r < n:

                count[nums[r]] = count.get(nums[r], 0) + 1

                while len(count) > goal:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += (r - l + 1)
                r += 1
            return res
        return atmost(k) - atmost(k-1)
