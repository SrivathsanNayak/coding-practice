class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #referred xor solution
        
        c = 0
        for i in s+t:
            c ^= ord(i)
            
        return chr(c)