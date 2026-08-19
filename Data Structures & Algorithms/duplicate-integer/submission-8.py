
class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        thisDict ={}
        for num in nums:
            if num in thisDict:
                return True
            thisDict[num] = True
        return False
            

