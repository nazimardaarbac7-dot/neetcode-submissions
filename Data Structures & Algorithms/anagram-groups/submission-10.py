from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key  = "".join(sorted(s))
            d[key].append(s) #  key -> [s,s2]
        return [x for x in d.values()]