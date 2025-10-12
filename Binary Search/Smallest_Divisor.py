import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """again do binary search from 1 to max(nums)"""
        def sum_divisor(num):
            Sum = 0
            for i in nums:
                Sum += math.ceil(i/num)
            return Sum 
        low , high = 1, max(nums)
        while low < high:
            mid = (low + high)//2
            x = sum_divisor(mid)
            if x <= threshold:
                high = mid
            else:
                low =mid + 1
        return low
