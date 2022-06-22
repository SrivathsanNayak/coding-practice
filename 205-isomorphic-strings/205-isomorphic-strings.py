class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            d = {}
            c = ''
            for i in range(len(s)):
                if s[i] in d.keys() and d[s[i]] != t[i]:
                    return False
                elif s[i] not in d.keys() and t[i] in d.values():
                    return False
                elif s[i] not in d.keys():
                    d[s[i]] = t[i]
            return True
            