class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = str(len(s))
            res += l + "#" + s
        return res
    def decode(self, s: str) -> List[str]: #  5#hello5#world
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            i = j+1
            res.append(s[i:i+l])
            i += l
        return res
