import heapq
class Solution:
    def maxSumCombinations(self, nums1, nums2, k):
      k_sum=[]
      for num1 in nums1:
        for num2 in nums2:
          heapq.heappush(k_sum,num1+num2)
          if len(k_sum) > k:
            heapq.heappop(k_sum)
      ans = []
      while k_sum:
        ans.append(heapq.heappop(k_sum))
      return ans.reverse
