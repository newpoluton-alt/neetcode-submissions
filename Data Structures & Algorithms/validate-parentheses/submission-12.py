class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        for i, v in enumerate(s):
            if v in closeToOpen:
                
                if not stack:
                    return False

                if stack[-1] == closeToOpen[v]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(v)

        return True if not stack else False
