from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_len = len(need)
        res = [-1,-1]
        res_len = float("inf")
        have = 0
        n= len(s)
        window = defaultdict(int)
        left = 0
        for right in range(n):
            right_char = s[right]
            window[right_char] += 1
            if right_char in need and window[right_char ] == need[right_char]:
                have += 1
            while have == need_len:
                if right - left +1 < res_len:
                    res_len = right-left+1
                    res = [left,right]
                left_char = s[left]
                window[left_char] -= 1
                left += 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
        left,right = res
        return s[left:right+1] if res != float("inf") else ""
                