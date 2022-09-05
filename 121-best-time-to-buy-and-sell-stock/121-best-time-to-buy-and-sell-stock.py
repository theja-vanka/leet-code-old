class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice: int = float('inf')
        profit: int = 0
        
        for price in prices:
            minprice = min(minprice, price)
            profit = max(profit, price-minprice)
        
        return profit