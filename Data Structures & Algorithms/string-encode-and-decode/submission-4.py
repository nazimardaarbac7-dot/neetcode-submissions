class Solution:

    def encode(self, strs: List[str]) -> str: #  5#hello5#world
        res = ""
        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    
    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0 
        while i < n:
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i += length
        return res
