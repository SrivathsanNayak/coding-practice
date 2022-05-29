class Solution(object):
    def isPalindrome(self, x):
        if (x < 0) or (str(x) != str(x)[::-1]):
            return False
        else:
            return True
        