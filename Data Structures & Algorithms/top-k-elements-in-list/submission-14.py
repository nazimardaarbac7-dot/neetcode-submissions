from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        sortedcounter = sorted(a.items(),key=lambda x:x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(sortedcounter[i][0])
        return res