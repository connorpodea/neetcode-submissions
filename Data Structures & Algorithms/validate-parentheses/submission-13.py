class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) > 0 and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        return False
