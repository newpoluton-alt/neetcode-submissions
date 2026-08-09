class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashmap = {}
        nums = list(set(nums))
        nums.sort()
        prevVal = nums[0]
        prevIndex = 0
        hashmap[prevIndex] = [prevVal]

        for i in range(1, len(nums)):
            if abs(nums[i] - prevVal) == 1:
                hashmap[prevIndex].append(nums[i])
            else:
                prevIndex = i
                hashmap[prevIndex] = [nums[i]]
            
            prevVal = nums[i]
        
        print(nums)
        print(hashmap)
            
        return max(list(map(lambda x: len(x), hashmap.values())))

        