class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        
        tmp = []
        
        for i in range(len(nums)):
            n = nums[i]
            rem = nums[:i] + nums[i+1:]
            
            for p in self.permute(rem):
                tmp.append([n] + p)
                
        return tmp
            
            