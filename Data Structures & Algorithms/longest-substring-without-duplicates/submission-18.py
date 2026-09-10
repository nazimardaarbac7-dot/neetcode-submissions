class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left = best= 0 
        for right in range(len(s)):
            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1 
                left += 1 
            best = max((right-left+1),best)
        return best
