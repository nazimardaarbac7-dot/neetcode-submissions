from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t is None :
            return ""
        left = 0
        window = defaultdict(int)
        need = Counter(t)
        have = 0
        res = [-1,-1]
        res_len = float("inf")
        need_len = len(need)
        for right in range(len(s)):
            right_char = s[right]
            window[right_char] += 1
            if right_char in need and window[right_char] == need[right_char]:
                have += 1
            while have == need_len:
                cur_len = right-left +1
                if cur_len < res_len:
                    res = [left,right]
                    res_len = cur_len
                left_char = s[left]
                window[left_char] -= 1
                left +=1
                if left_char in need and window[left_char] <need[left_char]:
                    have-=1
        left,right = res
        return s[left:right+1] if res_len < float("inf") else ""
