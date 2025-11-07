class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        Len = 0
        l,h = 0,0
        unique = set()
        while l < n and h < n:
            if s[h] not in unique:
                h +=1
                Len += 1
            if s[h] in unique:
                maxLen = max(maxLen,Len)
                Len = 0
                unique.remove(s[l])
                l += 1
        return maxLen
