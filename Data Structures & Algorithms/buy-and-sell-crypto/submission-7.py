class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit =0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                currP = prices[j] - buy
            
                maxProfit = max(maxProfit,currP)
        return maxProfit