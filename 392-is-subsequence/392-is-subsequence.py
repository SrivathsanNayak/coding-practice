class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            ptr = t.find(i)
            if ptr == -1:
                return False
            else:
                t = t[ptr + 1:]
        return True
        