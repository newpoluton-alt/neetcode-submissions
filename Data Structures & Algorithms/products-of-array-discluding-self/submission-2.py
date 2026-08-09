class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = [1] * n
        
        prefix = 1
        for i in range(n):
            hashmap[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            hashmap[i] *= suffix
            suffix *= nums[i]

        return hashmap