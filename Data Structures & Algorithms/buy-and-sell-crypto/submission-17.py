class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        m = 0
        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                p = prices[right] - prices[left]
                m = max(p,m)
        return m        