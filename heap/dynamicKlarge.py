import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_heap = []
        
        # Build a min heap of size at most k
        for num in nums:
            heapq.heappush(self.k_heap, num)
            if len(self.k_heap) > k:
                heapq.heappop(self.k_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_heap, val)
        if len(self.k_heap) > self.k:
            heapq.heappop(self.k_heap)
        
        # kth largest = smallest element inside min-heap
        return self.k_heap[0]
