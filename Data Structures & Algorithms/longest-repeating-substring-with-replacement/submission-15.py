from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uzunluk - maks tekrar < k olmalı 
        n = len(s)
        left = 0 
        best = 0
        window = defaultdict(int) 
        for right in range(n):
            window[s[right]] += 1 
            while (right-left+1) - max(window.values()) > k :
                window[s[left]] -= 1 
                left += 1
            best = max(best,(right-left+1))
        return best