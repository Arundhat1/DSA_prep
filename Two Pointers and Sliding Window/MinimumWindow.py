from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        formed = 0               # how many distinct chars meet required freq
        required = len(need)     # number of distinct chars required

        l = 0
        best_len = float("inf")
        best_l = 0  # start index of best window

        for r, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # try to shrink while window is valid
            while formed == required and l <= r:
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = l

                # remove left char and move left pointer
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1

        if best_len == float("inf"):
            return ""
        return s[best_l: best_l + best_len]
