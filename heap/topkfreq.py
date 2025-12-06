import heapq
"""just keep heap of size k ,heap based on the frequeny of occurence and associate the frequency to
 its number by making heap 2D """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 1) + 1 if num in count else 1

        # Step 2: Min heap of size k
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Extract top k frequent numbers
        return [num for freq, num in min_heap]
