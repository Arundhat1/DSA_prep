class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ invaraint was that median divides the sorted array into two equal parts . SO instead of merging two arrays which takes O(N) time
        what we do instead is to imagine partitioning into left and right part with equal numbers. We choose shortest array and then decides 
        how to divide it into left and right and accordingly divide another array so that left part and right part contains half of total
        . we do binary search on length of shortest array ,selected number decides this much will be in left part and remaining of the left part will 
        be covered by another array. how to decide to move to right or left or we have hit the answer? When we divide the chosen array and another array then 
         largest of left must be smaller or equal to smallest of right if this holds true then we have got it right other"""
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # ensure A is the smaller array
        if m > n:
            A, B, m, n = B, A, n, m

        total = m + n
        half = (total + 1) // 2  # +1 handles both even/odd cases

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # partition index in A
            j = half - i             # partition index in B

            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < m else float('inf')
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < n else float('inf')

            # correct partition found
            if A_left <= B_right and B_left <= A_right:
                if total % 2:  # odd
                    return max(A_left, B_left)
                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                right = i - 1  # move partition left
            else:
                left = i + 1   # move partition right
