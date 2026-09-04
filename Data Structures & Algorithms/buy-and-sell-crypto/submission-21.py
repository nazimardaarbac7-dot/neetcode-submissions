class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                best = max(best,profit)
        return best