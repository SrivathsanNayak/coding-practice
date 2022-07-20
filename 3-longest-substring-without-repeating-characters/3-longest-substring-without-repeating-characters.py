class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #sliding window
        chars = set()
        l = 0
        ans = 0
        
        for r in range(len(s)):
            #if duplicate char found
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            ans = max(ans, r - l + 1)
            
        return ans
        