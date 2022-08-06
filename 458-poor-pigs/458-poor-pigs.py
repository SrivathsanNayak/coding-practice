class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        #copied from top solution btw
        return int(ceil(log(buckets) / log(minutesToTest / minutesToDie + 1)))