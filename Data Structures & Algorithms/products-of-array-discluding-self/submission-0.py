class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce
        hashmap = {}
        for i in range(len(nums)):
            tempNums = nums[:]
            tempNums.pop(i)
            hashmap[i] = reduce(lambda x, y: x * y,  tempNums, 1)
            
        return list(hashmap.values())