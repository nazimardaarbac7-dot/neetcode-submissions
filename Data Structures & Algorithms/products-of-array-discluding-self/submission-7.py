class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [1] * n # [1,1,1,1], [10,2,4,3]
        prefix = 1
        for i in range(n): # 0,1,2,3
            r[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            r[i] *= postfix
            postfix *= nums[i]
        return r