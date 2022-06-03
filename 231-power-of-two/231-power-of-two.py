class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        #using bit manipulation from SO
        return ((n & (n - 1) == 0) and n != 0)
        #works as every power of 2 has only one bit set to 1
        #when subtracted, that bit becomes 0 and other bits become 1
        #so AND operation gives 0 if it is power of 2
        