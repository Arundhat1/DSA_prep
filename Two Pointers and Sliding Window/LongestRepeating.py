class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        res = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_count = max(max_count, count[s[r]])

            # if window becomes invalid (too many replacements needed)
            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res

