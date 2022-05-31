class Solution(object):
    def removeElement(self, nums, val):
        #using two pointers
        i = 0
        n = len(nums)
        while (i < n):
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
                #replace last element of array and reduce array size
                
            else:
                i += 1
                #move left pointer rightwards

        return n
        