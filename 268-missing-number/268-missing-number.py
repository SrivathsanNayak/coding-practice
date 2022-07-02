class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = len(nums)
        if nums == range(r + 1):
            return r + 1
        s = 0
        for i in nums:
            s ^= i
        for i in range(r+1):
            s ^= i
        return s
            