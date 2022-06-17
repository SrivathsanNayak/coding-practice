class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 2:
            nums.reverse()
            return
        
        pivot = len(nums) - 2
        
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
            
        #reached end but pivot unchanged
        #means array is reverse-sorted
        if pivot == -1:
            nums.reverse()
            return
        
        #swap values
        for i in range(len(nums) - 1, pivot, -1):
            if nums[pivot] < nums[i]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
                
        #reversing remaining elements after pivot
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        
        