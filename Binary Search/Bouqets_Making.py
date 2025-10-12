class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """ Here our approach will be to check or search from min(bloomDay) to max(bloomDay) 
        if by parrining k consecutinve flowers , bouquets can be summed up to m . We will do binary search
        after brute force search"""
        if len(bloomDay) < m * k:
            return -1
        def Can_bouqet(day):
            pair = 0
            bouqet = 0
            for flower in bloomDay:
                if flower <= day:
                    pair += 1
                else:
                    pair = 0
                if pair == k:
                    bouqet += 1
                    pair = 0
            return bouqet >= m
        low, high = min(bloomDay), max(bloomDay)
        min_day = -1
        while low < high:
            mid = (low+high)//2
            if Can_bouqet(mid):
                high = mid
            else:
                low = mid + 1
        return low if Can_bouqet(low) else -1

