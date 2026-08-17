class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            if (i>0) and (nums[i] == nums[i-1]):
                continue
            left = i+1 
            right = n -1

            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < 0 :
                    left +=1
                elif total >0:
                    right -=1
                else:
                    res.add((nums[left],nums[right],nums[i]))
                    left += 1
                    right -= 1
                    
        return [list(x)for x in res]
                    
