class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        left = 0 
        most = 0
        n = len(prices)
        for right in range(1,n):
            if prices[left] > prices[right]:
                left = right
                continue
            profit = prices[right] - prices[left]
            most = max(profit,most)
        return most