class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = nums

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums = sorted(self.nums, reverse=True)[:self.k]

    #     return self.nums[-1]
        
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # self.nums.append(val)
        # self.nums = sorted(self.nums, reverse=True)[:self.k]

        # return self.nums[-1]

        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]