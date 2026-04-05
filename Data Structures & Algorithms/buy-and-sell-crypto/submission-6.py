class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxSell = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            profit = prices[r] - prices[l]
            maxSell = max(maxSell, profit)
        return maxSell