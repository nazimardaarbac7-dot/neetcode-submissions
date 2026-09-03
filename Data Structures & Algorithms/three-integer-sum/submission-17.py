class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < 0 :
                    left += 1 
                elif total > 0 :
                    right -= 1
                else:
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1 
                    right -= 1 
        return [list(x) for x in res]


