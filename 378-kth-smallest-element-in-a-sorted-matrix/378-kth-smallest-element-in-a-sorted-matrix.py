class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_than_k(mid):
            cnt = 0
            for i in range(n):
                cnt += bisect_right(matrix[i], mid)
            return cnt
        
        while l < r:
            mid = (l + r) // 2
            if less_than_k(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l