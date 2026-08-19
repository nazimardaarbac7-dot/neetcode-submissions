class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        i = 0
        j = len(s)-1
        for i in range(len(s)//2):
            if s[i] != s[j]:
                return False
            j-=1
        return True