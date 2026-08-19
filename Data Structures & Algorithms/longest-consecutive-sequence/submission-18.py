class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0 
        numset = set(nums)
        for num in nums:
            if num-1 not in numset:
                current_number = num
                current_streak = 1
                while current_number+1 in numset:
                    current_number +=1
                    current_streak +=1
                best = max(best,current_streak)
        return best