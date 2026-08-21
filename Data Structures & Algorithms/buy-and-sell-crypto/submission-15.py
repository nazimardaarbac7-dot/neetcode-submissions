class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        left = 0 
        m = 0
        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
                continue
            
            profit = prices[right] - prices[left]
            m = max(m,profit)
        return m
