class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums = sorted(nums)
        for i in range(n):
            left = i + 1
            right = n-1
            while(left < right):
                total = nums[left] + nums[i] + nums[right]
                if total > 0 :
                    right -=1
                elif total <0:
                    left += 1
                else:
                    res.add((nums[left],nums[i],nums[right]))
                    right -=1
                    left += 1
        return [list(t) for t in res]
                
