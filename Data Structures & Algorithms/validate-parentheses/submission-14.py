class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
        