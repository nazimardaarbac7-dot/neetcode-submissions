class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = list()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        sorted_items = sorted(d.items(),key=lambda x:x[1],reverse=True)

        for i in range(k):
            l.append(sorted_items[i][0])
        return l


