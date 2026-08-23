from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uzunluk - tekrarlı  > k INVALID
        most = 0
        left = 0
        window = defaultdict(int) 
        n = len(s)
        for right in range(n):
            window[s[right]] += 1
            while (right-left+1)- max(window.values()) > k:
                window[s[left]] -=1
                left +=1
            most = max(most,right-left +1)
        return most