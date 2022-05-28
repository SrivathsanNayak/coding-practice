class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            firstIndex = nums.index(i)
            diff = target - i
            try:
                if diff in nums and nums.index(diff, firstIndex+1) != firstIndex:
                    return [firstIndex, nums.index(diff, firstIndex+1)]
            except ValueError:
                continue
        