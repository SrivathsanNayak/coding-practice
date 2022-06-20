class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ''.join(c.lower() for c in s if c.isalnum())
        if string == string[::-1]:
            return True
        else:
            return False
        