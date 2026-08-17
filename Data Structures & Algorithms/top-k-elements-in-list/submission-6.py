class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thisDict = {}
        result = []
        for num in nums:
            if num in thisDict:
                thisDict[num] +=1
            else:
                thisDict[num] = 1
        items_sorted = sorted(thisDict.items(), key = lambda item:item[1],reverse=True)
        for i in range(k):
            result.append(items_sorted[i][0])
        return result

