class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numset = set(nums)
        best = 0
        for num in numset:
            if num-1 not in numset:
                cn = num 
                cs = 1
                while cn+1 in numset:
                    cs += 1 
                    cn += 1
                best = max(cs,best)
        return best