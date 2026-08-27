from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left = 0 
        best = 0 
        for right in range(len(s)):
            #windowa al - > invalidleri çıkart -> kaydet
            window[s[right]] += 1
            while window[s[right]] > 1 :
                window[s[left]] -= 1 
                left += 1
            l = right - left + 1
            best = max(best,l)
        return best
