class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisDict = {}
        for i,num in  enumerate(nums):
            need = target - num
            if need in thisDict:
                return [thisDict[need],i]
            thisDict[num] = i
        return []