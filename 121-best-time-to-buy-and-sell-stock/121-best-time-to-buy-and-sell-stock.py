class Solution(object):
    def maxProfit(self, prices):
        #refer to top solution
        leftPtr = 0
        rightPtr = 1
        maxProfit = 0
        while rightPtr < len(prices):
            currentProfit = prices[rightPtr] - prices[leftPtr]
            if currentProfit > 0:
                maxProfit = max(currentProfit, maxProfit)
            else:
                leftPtr = rightPtr
            rightPtr += 1
        return maxProfit