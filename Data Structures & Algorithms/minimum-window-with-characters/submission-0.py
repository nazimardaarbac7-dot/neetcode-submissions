from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t is None:
            return ""
        need = Counter(t)
        have = 0
        need_count = len(need)
        window = defaultdict(int)
        res = [-1,-1]
        res_len = float("inf")
        left = 0 
        for right in range(len(s)):
            char = s[right]
            window[char] += 1 
            if char in need and window[char] == need[char]:
                have += 1 
            while need_count  == have:
                if (right - left + 1) < res_len:
                    res_len = right-left +1
                    res = [left,right]
                left_char = s[left]
                window[left_char] -= 1
                left += 1 
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1 
        left,right = res 
        return s[left:right+1] if res_len != float("inf") else ""

