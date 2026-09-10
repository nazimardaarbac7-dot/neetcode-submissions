from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = Counter(t)
        have = 0
        res = [-1,-1]
        res_len = float("inf")
        left = 0 
        for right in range(len(s)):
            rightChar = s[right]
            window[rightChar] += 1 
            if rightChar in need and window[rightChar] == need[rightChar]:
                have += 1 
            while have == len(need):
                if (right-left+1) < res_len:
                    res_len = right-left+1
                    res = [left,right]
                leftChar = s[left]
                left += 1
                window[leftChar] -= 1
                
                if leftChar in need and window[leftChar] < need[leftChar]:
                    have -= 1 
        left,right = res
        return s[left:right+1] if res_len is not float("inf") else ""
                