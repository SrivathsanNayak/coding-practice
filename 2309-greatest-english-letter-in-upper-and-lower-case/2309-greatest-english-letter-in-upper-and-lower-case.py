class Solution(object):
    def greatestLetter(self, s):
        greatUpper = ''
        for i in s:
            if 'A' <= i <= 'Z' and i.lower() in s:
                greatUpper = max(greatUpper, i)
        return greatUpper
        