class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2


            if mid % 2 == 1:
                mid -= 1

            # Compare mid with its next element
            if nums[mid] == nums[mid + 1]:
                # Correct pair → single lies to the right
                left = mid + 2
            else:
                # Broken pair → single lies to the left (including mid)
                right = mid

        return nums[left]
