class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = int(''.join(map(str, digits))) + 1
        return [int(x) for x in str(s)]
            