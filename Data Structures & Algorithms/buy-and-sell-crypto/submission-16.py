class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        mp = 0
        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                p = prices[right] - prices[left]
                mp = max(p,mp)
        return mp