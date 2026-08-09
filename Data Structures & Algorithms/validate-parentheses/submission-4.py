class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2 or len(s) % 2 != 0:
            return False

        stack = []
        allowed_symbols = ["{", "[", "("]
        not_velcomed_symbols = ["}", ")", "]"]
        an_map = {"{":"}", "(": ")", "[":"]"}
        na_map = {"}":"{", "]":"[", ")":"("}

        for i, ch in enumerate(s):
            if ch in allowed_symbols:
                stack.append(ch)
                continue
            if any([ch in not_velcomed_symbols and na_map[ch] not in s]):
                return False
                
            if ch in not_velcomed_symbols and len(stack) == 0:
                return False

            if ch == "}" and stack[-1] == "{":
                stack.pop(-1)
            if ch == "]" and stack[-1] == "[":
                stack.pop(-1)
            if ch == ")" and stack[-1] == "(":
                stack.pop(-1)

        
        return True if len(stack) == 0 else False