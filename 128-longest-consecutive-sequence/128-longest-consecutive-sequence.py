class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        curLen, maxLen = 0, 0
        for i in numset:
            if (i - 1) not in numset:
                curLen = 0
                while (i + curLen) in numset:
                    curLen += 1
            maxLen = max(maxLen, curLen)
        return maxLen