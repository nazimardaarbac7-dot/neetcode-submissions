class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = ( left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # sol taraf sıralı
                if nums[left] <= target < nums[mid]: # sol sıralı taraf içinde target var mı
                    right = mid -1 
                else:
                    left = mid + 1 
            else: # sağ sıralı
                if nums[mid] < target  <= nums[right]: #sağ sıralı tarafta mı
                    left = mid + 1
                else:
                    right = mid - 1
        return -1