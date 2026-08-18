class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisDict = {}
        for index,value in enumerate(nums):
            need = target - value
            if need in thisDict:
                return [thisDict[need],index]
            else:
                thisDict[value] = index
        