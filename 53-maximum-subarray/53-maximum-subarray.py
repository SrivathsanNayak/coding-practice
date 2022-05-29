class Solution(object):
    def maxSubArray(self, nums):
        #Kadane algo
        currentSum = bestSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            bestSum = max(currentSum, bestSum)
        return bestSum
        