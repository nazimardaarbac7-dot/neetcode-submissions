class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisDict = {}
        result = []
        for i,v in enumerate(nums):
            need = target - v 
            if need in thisDict:
                return [thisDict[need],i]
            thisDict[v] = i
