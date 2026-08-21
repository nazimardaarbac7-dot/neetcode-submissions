from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        m = 0
        l = 0 
        for r in range(len(s)):
            window[s[r]] +=1    # window'a al
            while window[s[r]] > 1 : #invalid kontrolu 
                window[s[l]] -= 1
                l += 1
            m = max(m,(r-l+1))                                #valid
        return m