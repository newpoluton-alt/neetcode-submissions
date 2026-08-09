class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        if len(s) < len(t):
            return ""
        
        if s == t:
            return t
        
        if t in s:
            return t

        need = defaultdict(int)

        for i in range(len(t)):
            need[t[i]] += 1
        
        window = {}
        required = len(need)
        have = 0

        res = (float("inf"), 0, 0)
        left = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == required:
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                left += 1
        length, l, r = res
        return "" if length == float("inf") else s[l:r+1]

        

