class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        best = 0
        for num in numset:
            if (num-1) not in numset:
                current_num = num
                current_streak = 1 
            
                while (current_num+1) in numset:
                    current_num += 1 
                    current_streak +=1 
                best = max(best,current_streak)
        return best