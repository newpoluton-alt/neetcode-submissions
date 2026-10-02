class Solution:
    def __init__(self):
        self.h = []
        
    def isHappy(self, n: int) -> bool:
        t = 0
        
        for s in str(n):
            s = int(s)
            t += s ** 2
        
        if t == 1:
            return True
        if self.h and t in self.h:
            return False

        self.h.append(t)
        return self.isHappy(t)