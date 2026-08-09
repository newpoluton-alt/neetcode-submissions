class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = hashmap.get(num, 0) + 1

        sorted_hashmap_values = list(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        k_frequent_elements = [num for num, freq in sorted_hashmap_values[:k]]

        return k_frequent_elements