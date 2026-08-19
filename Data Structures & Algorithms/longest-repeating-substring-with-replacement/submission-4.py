from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxf = 0
        longest = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] +=1
            maxf = max(count.values()) if count else maxf
            if (right-left+1) - maxf > k:
                count[s[left]] -=1
                left +=1
            
            longest = max((right-left+1),longest)
        return longest