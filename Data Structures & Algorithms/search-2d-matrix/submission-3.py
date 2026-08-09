class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def _binary_search(nums: List[int], target: int) -> bool:
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
            
            return False

        return any([_binary_search(nums, target) for nums in matrix])