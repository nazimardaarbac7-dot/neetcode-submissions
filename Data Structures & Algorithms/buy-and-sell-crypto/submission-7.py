class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        n = len(prices)
        i = 0 
        mostProfit= 0
        for j in range(1,n):
            if prices[i] > prices[j]:
                i = j
            else:
                profit = prices[j] - prices[i]
                mostProfit = max(mostProfit,profit)
        return mostProfit