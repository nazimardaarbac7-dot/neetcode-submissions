from collections import defaultdict,Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        window = defaultdict(int)
        need = Counter(t)
        have = 0 
        res = [-1,-1]
        res_len = float("inf")
        left = 0
        for right in range(n):
            right_char = s[right]
            window[right_char] += 1 
            if right_char in need and window[right_char] == need[right_char]:
                have += 1
            while len(need) == have:
                if res_len > (right-left+1):
                    res_len = (right-left +1)
                    res = [left,right]
                left_char = s[left]
                window[left_char] -= 1
                left += 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -=1 
        left,right = res
        return s[left:right+1] if res_len is not float("inf") else ""


