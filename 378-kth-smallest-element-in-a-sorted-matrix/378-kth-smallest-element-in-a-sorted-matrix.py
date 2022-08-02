class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        tmp = []
        for i in matrix:
            tmp.extend(i)
        tmp.sort()
        return tmp[k - 1]
            