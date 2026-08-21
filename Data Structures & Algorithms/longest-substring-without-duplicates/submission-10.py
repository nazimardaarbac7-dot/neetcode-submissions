from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # windowa al -> invalidleri çıkart -> valid -> kaydet
        window = defaultdict(int)
        left = 0
        n = len(s)
        m = 0
        for right in range(n):
            right_char = s[right]
            window[right_char] += 1
            while window[right_char] > 1:
                window[s[left]] -= 1
                left +=1
            m = max(m,right - left +1)
        return m