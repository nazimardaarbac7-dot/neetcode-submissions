from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thisDict = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            thisDict[key].append(string)
        return list(thisDict.values())

