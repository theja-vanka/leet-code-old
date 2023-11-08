class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit: int = 0
        buy_index:int = 0
        sell_index: int = 1

        while sell_index < len(prices):
            current_profit: int = prices[sell_index] - prices[buy_index]

            if prices[buy_index] < prices[sell_index]:
                max_profit = max(current_profit, max_profit)
            else:
                buy_index = sell_index
            sell_index += 1
        
        return max_profit


        