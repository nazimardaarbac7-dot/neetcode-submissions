class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_index = 0
        right_index = 1

        while(right_index < len(prices) ):
            buy = prices[left_index]
            sell = prices[right_index]

            cur_profit = sell - buy
            if cur_profit < 0:
                left_index = right_index;
                right_index+=1
            else:
                right_index+=1
            max_profit=max(max_profit,cur_profit)
        return max_profit