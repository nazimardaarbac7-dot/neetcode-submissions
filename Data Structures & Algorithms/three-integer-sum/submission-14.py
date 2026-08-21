class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i+1
            right = len(nums) -1
            while left < right:
                total = nums[right] + nums[left] + nums[i]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1 
                else:
                    s.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
        return [list(x) for x in s]