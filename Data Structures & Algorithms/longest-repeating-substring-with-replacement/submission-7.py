from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maksfrekans - uzunluk > k -> invalid
        left = 0
        n = len(s)
        maxl = 0
        count = defaultdict(int)
        for right in range(n):
            count[s[right]] += 1
            while (right - left +1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            maxl = max((right-left+1),maxl)
        return maxl
