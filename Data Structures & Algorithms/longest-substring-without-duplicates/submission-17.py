from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        best = 0
        window = defaultdict(int)
        for right in range(n):
            window[s[right]] += 1
            while window[s[right]] > 1 :
                window[s[left]] -= 1 
                left += 1 
            best = max((right - left + 1),best)
        return best