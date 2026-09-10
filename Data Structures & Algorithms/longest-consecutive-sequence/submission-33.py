class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        best = 0
        for num in numset:
            if num-1 not in numset:
                cs = 1 
                cn = num 
                while cn + 1 in numset:
                    cs += 1 
                    cn += 1
                best = max(best,cs)
        return best