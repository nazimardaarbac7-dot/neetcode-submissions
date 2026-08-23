from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window - > valid - > save
        window = defaultdict(int)
        n = len(s)
        most = 0
        left   = 0
        for right in range(n):
            window[s[right]] += 1
            while window[s[right]] > 1 :
                window[s[left]] -= 1
                left += 1
            most = max(most,(right-left+1))
        return most
