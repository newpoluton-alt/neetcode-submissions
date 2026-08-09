class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # [[element, index]]
        
        for i, e in enumerate(temperatures):
            while stack and e > stack[-1][0]:
                elem, ind = stack.pop()
                results[ind] = i - ind
            
            stack.append([e, i])

        return results