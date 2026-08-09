class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        
        if len(nums) == 1:
            return nums

        if len(nums) < k:
            return []

        for i, e in enumerate(nums[: len(nums) - k + 1]):
            max_v = max(nums[i:k+i])
            answer.append(max_v)

        return answer