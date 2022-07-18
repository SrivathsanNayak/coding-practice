class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, low, high, target):
            
            if high >= low:
                
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    return binarySearch(nums, low, mid - 1, target)
                
                elif nums[mid] < target:
                    return binarySearch(nums, mid + 1, high, target)
                
            else:
                
                return -1
            
        return binarySearch(nums, 0, len(nums) - 1, target)