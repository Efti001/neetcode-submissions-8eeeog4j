class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buying low, selling high
        l = 0 #buying
        maxProfit = 0
        for r in range(len(prices)): #sliding window using r pointer
            if  prices[l] >= prices[r]:
                l = r
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        return maxProfit