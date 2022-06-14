class Solution(object):
    def maxProfit(self, prices):
        minPrice = float('inf')
        maxProfit = 0
        
        for price in prices:
            minPrice = min(minPrice, price)
            curProfit = price - minPrice
            maxProfit = max(curProfit, maxProfit)
            
        return maxProfit
            