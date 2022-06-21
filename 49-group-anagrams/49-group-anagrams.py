class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        res = defaultdict(list)
        
        #sort all strings
        #if anagram, add grouped list as value
        
        for i in strs:
            s = ''.join(sorted(i))
            if s not in res:
                res[s] = [i]
            else:
                res[s] += [i]
        
        return res.values()