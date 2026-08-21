class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            need = target - v
            if need in d:
                return [d[need],i]
            d[v] = i
        