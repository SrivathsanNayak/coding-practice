class Solution(object):
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums) 
        el = 1
        for i in range(len(nums)):
            el *= nums[i]
            pre[i] = el
        el = 1
        for i in range(len(nums) - 1, 0, -1):
            el *= nums[i]
            post[i - 1] = el
        
        ans[0] = post[0]
        for i in range(1, len(nums)):
            ans[i] = pre[i - 1] * post[i]
        
        return ans
            
                