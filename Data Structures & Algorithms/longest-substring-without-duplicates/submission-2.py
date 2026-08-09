class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        r = 0
        ans = 0
        hashset = []

        while(r < len(s)):
            if(s[r] not in hashset):
                hashset.append(s[r])
                r += 1
                ans = max(ans, len(hashset))
            else:
                while(s[r] in hashset):
                    hashset.pop(0)

        return ans