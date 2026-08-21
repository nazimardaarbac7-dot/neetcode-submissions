from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1,-1]
        left = 0 
        need = Counter(t)
        window = defaultdict(int)
        need_len = len(need)
        have = 0
        res_len = float("inf")
        for right in range(len(s)):
            right_char = s[right]
            window[right_char] += 1
            if right_char in need and window[right_char] == need[right_char]:
                have += 1
            while have == need_len:
                current_len = right -left +1
                if current_len < res_len:
                    res_len = current_len
                    res = [left,right]
                left_char = s[left]
                window[left_char] -= 1
                left += 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
        left,right = res
        return s[left:right + 1] if res_len != 0 else ""


