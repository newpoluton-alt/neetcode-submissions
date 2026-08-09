class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from math import trunc

        if len(tokens) < 3:
            return int(tokens[0])
        
        division = lambda x, y: trunc(x / y)
        multi = lambda x, y: x * y
        substraction = lambda x, y: x - y
        add = lambda x, y: x + y

        ol_map = {"+": add, "*": multi, "/": division, "-": substraction}
        ans = 0
        stack = []

        for i, e in enumerate(tokens):
            if e not in ol_map.keys():
                stack.append(int(e))
            else:
                if stack:
                    b = stack.pop(-1)
                    a = stack.pop(-1)

                    ans = ol_map[e](a, b)
                    stack.append(ans)
            print(stack)

        return stack[-1]