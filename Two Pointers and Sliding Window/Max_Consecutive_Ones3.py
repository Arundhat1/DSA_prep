class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initialize left pointer of sliding window and count of zeros in window
        left = 0
        zero_count = 0
      
        # Iterate through array with implicit right pointer (index)
        for right in range(len(nums)):
            # If current element is 0, increment zero count
            # (x ^ 1 converts 0->1 and 1->0, so we count zeros)
            if nums[right] == 0:
                zero_count += 1
          
            # If we have more than k zeros, shrink window from left
            if zero_count > k:
                # If the left element being removed is 0, decrement zero count
                if nums[left] == 0:
                    zero_count -= 1
                # Move left pointer forward
                left += 1
      
        # The window size at the end is the maximum valid window
        # (right pointer is at len(nums)-1, so window size is len(nums) - left)
        return len(nums) - left
