class Solution:
    def mySqrt(self, x: int) -> int:
        found = False
        low, high = 1, x
        while high >= low:
            mid = (low+high)//2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                low = mid+1
            else:
                high = mid -1
        return high
