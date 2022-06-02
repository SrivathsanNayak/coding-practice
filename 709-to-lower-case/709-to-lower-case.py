class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        lower = ""
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                lower += chr(ord(i) + 32)
            else:
                lower += i
        return lower
                