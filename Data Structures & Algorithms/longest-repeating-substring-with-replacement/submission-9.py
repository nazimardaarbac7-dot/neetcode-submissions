from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uzunluk - maksFrekans > k ise INVALID
        left = 0
        window = defaultdict(int)
        n = len(s)
        m = 0
        maxf = 0
        for right in range(n):
            window[s[right]] += 1
            maxf = max(window[s[right]],maxf)
            while (right - left +1) - maxf > k:
                window[s[left]] -= 1
                left += 1
            m = max(right - left+1,m)
        return m
