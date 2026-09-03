class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        numset = set(nums)
        for num in numset:
            if num-1 not in numset:
                cn = num
                cs = 1 
                while cn+1 in numset:
                    cn+= 1 
                    cs+= 1 
                best = max(cs,best)
        return best
