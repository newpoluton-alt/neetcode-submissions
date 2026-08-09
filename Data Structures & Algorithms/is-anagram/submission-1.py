class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = {l:0 for l in set([e for e in s+t])}
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            alphabet[t[i]] -= 1
            alphabet[s[i]] += 1
        for n in alphabet.values():
            if n != 0:
                return False
        else:
            return True
        