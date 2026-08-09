class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        prevLeftMaxHeight = height[l]
        prevRightMaxHeight = height[r]
        answer = 0
        while(any([height[l] <= e for e in height[l+1:]])):

            l += 1
            prevLeftMaxHeight = max(prevLeftMaxHeight, height[l])
            if height[l] < prevLeftMaxHeight:
                answer += (prevLeftMaxHeight - height[l])
        
        while(any([height[r] <= e for e in height[l:r-1]])):
            r -= 1
            prevRightMaxHeight = max(prevRightMaxHeight, height[r])
            if height[r] < prevRightMaxHeight:
                answer += (prevRightMaxHeight - height[r])
            
        return answer