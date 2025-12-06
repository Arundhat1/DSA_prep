import heapq
""" in this we used sliding window and max_heap"""
class Solution:
    def maxSlidingWindow(self, nums, k):
        heap = []  # will store (-value, index)
        ans = []

        for i, num in enumerate(nums):
            # push current element
            heapq.heappush(heap, (-num, i))

            # if window not reached k yet, just continue
            if i < k - 1:
                continue

            # pop elements that are outside the window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # current max
            ans.append(-heap[0][0])

        return ans
