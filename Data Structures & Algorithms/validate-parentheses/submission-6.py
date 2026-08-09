class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        allowed_symbols = ["{", "[", "("]
        not_velcomed_symbols = ["}", ")", "]"]
        na_map = {"}":"{", "]":"[", ")":"("}

        if len(s) < 2 or len(s) % 2 != 0:
            return False

        if any([ch in not_velcomed_symbols and na_map[ch] not in s for ch in s]):
            return False

        for i, ch in enumerate(s):
            if ch in allowed_symbols:
                stack.append(ch)
                continue

            if ch in not_velcomed_symbols and len(stack) == 0:
                return False

            reverse_ch = na_map[ch]

            if ch in not_velcomed_symbols and stack[-1] == na_map[ch]:
                stack.pop(-1)

        
        return True if len(stack) == 0 else False