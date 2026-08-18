class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        j = len(s) - 1
        for i in range(len(s)//2):
            if s[i] != s[j]:
                return False
            j -= 1
        return True