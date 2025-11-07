class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def atMost(k):
            if k < 0:
                return 0
            n = len(s)
            count = {}
            res = 0
            l = 0
            
            for r in range(n):
                count[s[r]] = count.get(s[r], 0) + 1
                
                while len(count) > k:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        del count[s[l]]
                    l += 1
                
                # Every substring ending at r with ≤ k distinct chars
                res += (r - l + 1)
            
            return res
        
        # Exactly 3 distinct = atMost(3) - atMost(2)
        return atMost(3) - atMost(2)
