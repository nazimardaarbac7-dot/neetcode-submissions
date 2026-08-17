class Solution:

    def encode(self, strs: List[str]) -> str: #hello world
        s = ""
        for string in strs:
            s += str(len(string)) + '#' + string
        return s
    
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i 
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            result.append(s[i:i+length])
            i += length
        return result

