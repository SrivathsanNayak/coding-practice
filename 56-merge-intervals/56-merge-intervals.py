class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        ans = [intervals[0]]
        
        for start, end in intervals[1:]:
            latestEnd = ans[-1][1]
            
            if start <= latestEnd:
                #compare ending elements of merging intervals
                ans[-1][1] = max(latestEnd, end)
            
            else:
                ans.append([start, end])
                
        return ans
        