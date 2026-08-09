class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        arr = [1, 1]

        n -= 1
        while n >= 1:
            new_n = sum(arr[:2])
            arr.insert(0, new_n)
            n -= 1

        return arr[0]