class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        thisdict = {}
        for number in nums:
            if number in thisdict:
                return True
            thisdict[number] = True
        return False