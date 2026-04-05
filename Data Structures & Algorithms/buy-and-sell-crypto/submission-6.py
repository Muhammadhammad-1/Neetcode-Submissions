class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices) < 2:
            return 0
            
        minProfit = float('inf')
        maxProfit = 0
        
        for price in prices:
            minProfit = min(minProfit,price)
            maxProfit = max(maxProfit,price - minProfit)
        return maxProfit
