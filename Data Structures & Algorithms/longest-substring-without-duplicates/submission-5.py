class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        hashset = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in hashset:
                l = max(l, hashset[s[r]] + 1)

            hashset[s[r]] = r

            res = max(res, r - l + 1)

        return res