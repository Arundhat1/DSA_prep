class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count_odd(goal):
            if goal <0 :
                return 0
            n = len(nums)
            count = 0
            res = 0
            l = 0
            for r in range(n):
                if nums[r] % 2 == 1:
                    count += 1
                
                while count > goal:
                    if nums[l] % 2 == 1 and l < n:
                        count -= 1
                    l += 1
                res += (r-l+1)
                
            return res
        return count_odd(k) - count_odd(k-1)
