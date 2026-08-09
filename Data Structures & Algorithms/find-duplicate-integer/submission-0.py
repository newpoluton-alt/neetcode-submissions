class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashVal = {}

        for i, e in enumerate(nums):
            hashVal[e] = hashVal.get(e, 0) + 1
            
            if hashVal[e] > 1:
                return e
        return 0