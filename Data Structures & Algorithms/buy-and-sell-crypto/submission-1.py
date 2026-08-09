class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        profit = 0

        for i in range(len(prices)):
            minVal = min(prices[i], minVal)

            profit = max(profit, prices[i] - minVal)
        
        return profit
        