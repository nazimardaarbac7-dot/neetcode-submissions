from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        n = len(s)
        longest = 0
        maxF = 0
        for right in range(n):
            count[s[right]] +=1
            maxF = max(count[s[right]] , maxF) 
            while (right - left + 1 )- maxF > k :
                count[s[left]] -= 1 
                left += 1 
            longest = max ((right - left + 1 ),longest)
        return longest
