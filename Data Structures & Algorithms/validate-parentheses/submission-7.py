class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        allowed_symbols = ["{", "[", "("]
        not_velcomed_symbols = ["}", ")", "]"]
        na_map = {"}":"{", "]":"[", ")":"("}

        if len(s) < 2 or len(s) % 2 != 0:
            return False

        if any([ch in na_map.keys() and na_map[ch] not in s for ch in s]):
            return False

        for i, ch in enumerate(s):
            if ch in na_map.values():
                stack.append(ch)
                continue

            if ch in na_map.keys() and len(stack) == 0:
                return False

            if ch in na_map.keys() and stack[-1] == na_map[ch]:
                stack.pop(-1)

        
        return True if len(stack) == 0 else False