from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thisDict = defaultdict(int)
        res = []
        for num in nums:
            thisDict[num] += 1 
        items_sorted = sorted(thisDict.items(),key = lambda x :x[1],reverse=True)
        for i in range(k):
            res.append(items_sorted[i][0])
        return res