class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        answer = dict(sorted(hashmap.items(), key= lambda kv: kv[1],reverse = True))
        return sorted(list(answer.keys())[:k])