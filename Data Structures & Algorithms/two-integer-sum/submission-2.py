class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remained = target - nums[i]
            if remained in hashmap.keys():
                return [hashmap[remained], i]
            hashmap[nums[i]] = i
        else:
            return []