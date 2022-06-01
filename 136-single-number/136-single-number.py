class Solution(object):
    def singleNumber(self, nums):
        
        #using xor method
        a = nums[0]
        for i in range(1, len(nums)):
            a ^= nums[i]
        return a