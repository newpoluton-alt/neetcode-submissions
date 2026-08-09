class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            answer = {}
            if len(nums) == 3:
                if sum(nums) != 0:
                    return []
                else:
                    return [nums]

            for i in range(len(nums)):
                l, r = 0, len(nums) - 1

                while l < r:
                    if i == l:
                        l += 1
                        
                    if i == r:
                        r -= 1

                    if sum([nums[i], nums[l], nums[r]]) < 0:
                        l += 1
                    elif sum([nums[i], nums[l], nums[r]]) > 0:
                        r -= 1
                    elif sum([nums[i], nums[l], nums[r]]) == 0:
                        subAns = [nums[i], nums[l], nums[r]]
                        subAns.sort()
                        sortedKeys = [i, l, r]
                        uniqueKey = f"{sortedKeys[0]},{sortedKeys[1]},{sortedKeys[2]}"
                        if uniqueKey not in answer and subAns not in answer.values() and l != r:
                            answer[uniqueKey] = subAns
                        l += 1
                        r -= 1
                print(answer)
            else:
                return list(answer.values())
