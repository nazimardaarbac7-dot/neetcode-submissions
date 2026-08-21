from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res  = []
        for num in nums:
            d[num] += 1
        s_i = sorted(d.items(),key= lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(s_i[i][0])
        return res
