class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        sd = sorted(d.items(), key = lambda x:x[1], reverse = True)
        
        return [sd[i][0] for i in range(k)]
        