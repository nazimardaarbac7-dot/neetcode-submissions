class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum() )
        j = 0
        for i in range(len(s)//2):
            j -=1
            if s[j] != s[i]:
                return False
        return True

            