class Solution: # [4,5,6,7,2]
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left <  right:
            mid = (right + left) // 2
            if nums[mid]  > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

        
