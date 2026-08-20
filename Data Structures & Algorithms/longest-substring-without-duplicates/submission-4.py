from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        count = defaultdict(int)
        m = 0
        n = len(s)
        for right in range(n):
            count[s[right]] += 1 
            while count[s[right]] > 1 :
                count[s[left]] -= 1
                left += 1
            m = max(m,(right - left +1))
        return m