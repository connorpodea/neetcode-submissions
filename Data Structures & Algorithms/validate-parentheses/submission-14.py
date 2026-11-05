class Solution:
    def isValid(self, s: str) -> bool:
        # Stores all opening braces to compute valid.
        stack = []

        # Identify which brackets go together.
        pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        # Loop through each bracket. If its an opening, push it to the stack.
        # If its a closing, pop the top of the stack, and determine if its a proper
        # pair with the current bracket. If so continue, else return false.
        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) > 0 and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False

        # If there are an odd number of chars, or somehow the stack is non-empty
        # at the end of the algorithm, the string is not valid.
        if len(stack) == 0:
            return True
        else: 
            return False
