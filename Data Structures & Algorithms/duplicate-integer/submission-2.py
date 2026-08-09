class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = []
        for i, num in enumerate(nums):
            if num in hashset:
                return True
            else:
                hashset.append(num)
        else:
            return False