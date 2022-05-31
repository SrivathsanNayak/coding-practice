class Solution(object):
    def intersect(self, nums1, nums2):
        common = []
        if len(nums1) >= len(nums2):
            for i in nums1:
                if i in nums2:
                    common.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    common.append(i)
                    nums1.remove(i)
        return common
