class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        hashmap = {}
        calc_vol = lambda l, r: min(heights[l], heights[r]) * (r - l)
        hashmap[f"{l},{r}"] = calc_vol(l, len(heights) - 1)

        while(l < r):
            is_cur_lr_big = max(list(hashmap.values()))

            if heights[l] <= heights[r]:
                l += 1
                hashmap[f"{l},{r}"] = calc_vol(l, r)

            else:
                r -= 1
                hashmap[f"{l},{r}"] = calc_vol(l, r)

        print(hashmap)
        return max(hashmap.values())
        