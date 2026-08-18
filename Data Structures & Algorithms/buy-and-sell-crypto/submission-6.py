class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        i = 0
        mostProfit = 0
        n = len(prices)
        for j in range(n):
            if prices[j] < prices[i]:
                i = j
            else:
                profit = prices[j] - prices[i]
                mostProfit = max(profit,mostProfit)
        return mostProfit
