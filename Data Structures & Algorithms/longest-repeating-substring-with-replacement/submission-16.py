class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uzunluk - maxfrequency >  k
        best = 0
        window = defaultdict(int)
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1

            l = right-left+1
            best = max(l,best)
        return best