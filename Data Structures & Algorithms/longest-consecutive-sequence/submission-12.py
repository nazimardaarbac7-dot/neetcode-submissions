class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        bestStreak = 0
        current_number = 0 
        current_streak = 0
        for num in numset:
            if num-1 not in numset:
                current_number = num
                current_streak = 1
                while current_number+1 in numset:
                    current_number +=1
                    current_streak +=1
            bestStreak = max(current_streak,bestStreak)
        return bestStreak
