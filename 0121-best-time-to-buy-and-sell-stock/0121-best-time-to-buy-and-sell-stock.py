class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=prices[0]
        profit=0
        for price in prices:
            min_value=min(min_value,price)
            profit=max(profit,price-min_value)  
        return profit      
        