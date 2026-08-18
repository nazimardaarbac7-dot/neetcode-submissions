class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thisDict = {}
        res = []
        for num in nums:
            if num in thisDict:
                thisDict[num] +=1
            else:
                thisDict[num] = 1
        sorted_items = sorted(thisDict.items(),key = lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
