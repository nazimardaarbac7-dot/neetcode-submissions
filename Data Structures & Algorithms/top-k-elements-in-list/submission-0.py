class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        lis = sorted(d.items(),key= lambda x:x[1])
       
        lst =[]
        for item in lis:
            lst.append(item[0])
        lst.reverse()
        return lst[:k]



        