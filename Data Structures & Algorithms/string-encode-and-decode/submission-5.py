class Solution:

    def encode(self, strs: List[str]) -> str: #  5#hello5#world
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j +=1
            l = int(s[i:j])
            i = j+1
            res.append(s[i:i+l])
            i += l
        return res