class Solution(object):
    def merge(self, nums1, m, nums2, n):
        extra = len(nums1) - m
        for i in range(extra):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        