class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower().replace(" ","")
        for l in "!?,.':;":
            strs = strs.replace(l,"")

        print(strs)
        if strs == strs[::-1]:
            return True
        else:
            return False
        