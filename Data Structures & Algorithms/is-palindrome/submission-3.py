class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum() )
        reversed_string = s[::-1]
        return s == reversed_string

            