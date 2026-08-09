class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = sorted(list(zip(position, speed)), key = lambda x: x[0], reverse = True)
        stack = []
        time = lambda p, s: (target - p)/s

        for i, (p, s) in enumerate(posSpeed):
            stack.append(time(p, s))
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
            