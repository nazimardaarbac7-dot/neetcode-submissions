class Solution:
    def isValid(self, s: str) -> bool:# []
        stack = []
        pairs = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        for char in s:
            if char in "([{": 
                stack.append(char)
            else:
                if not stack:
                    return False
                if pairs[char] != stack[-1]:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False