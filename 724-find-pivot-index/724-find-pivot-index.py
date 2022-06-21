class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lSum = 0
        rSum = sum(nums) - nums[0]
        i = 1
        
        if lSum == rSum:
            return 0
        
        while i < len(nums):
            lSum += nums[i - 1]
            rSum -= nums[i]
            if lSum == rSum:
                return i
            i += 1
        
        if i == len(nums) and lSum == 0:
            return i - 1
        
        return -1
            