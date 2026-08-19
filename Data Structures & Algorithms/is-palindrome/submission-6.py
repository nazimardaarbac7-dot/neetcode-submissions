class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        n = len(s)
        left = 0
        j = n-1
        for i in range(n//2):
            if s[i] != s[j]:
                return False
            j -= 1
        return True