class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) < 3 and s1 in s2:
            return True

        for i in range(len(s2) - len(s1) + 1):
            if sorted(s1) == sorted(s2[i:i+len(s1)]):
                return True
        else:
            return False