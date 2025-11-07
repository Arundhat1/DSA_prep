class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n - k

        # Base case: take all cards
        if window_size == 0:
            return total

        # Step 1: initial window sum
        curr_sum = sum(cardPoints[:window_size])
        min_sum = curr_sum

        # Step 2: slide window
        for i in range(window_size, n):
            curr_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, curr_sum)

        # Step 3: total - min_subarray_sum
        return total - min_sum


