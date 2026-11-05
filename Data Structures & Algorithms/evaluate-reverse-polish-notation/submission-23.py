class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a set of operations to easily distinguish it from values.
        ops = {"+", "-", "*", "/"}
        # A stack storing pre and post computated values.
        vals = []

        # Loop through all of the tokens, pushing it to the top of the stack when its an integer.
        # and taking computing the arithmetic of the top 2 elements when the token is an operation.
        for token in tokens:
            if token in ops :
                val2 = vals.pop()
                val1 = vals.pop()
                vals.append(self.compute(token, val1, val2))
                continue # Dont push the token to the stack (reserved for integer values).
            vals.append(int(token))

        return vals[0]

    # Helper function
    def compute(self, op: str, val1: int, val2: int) -> int:
        match op:
            case "+":
                return val1 + val2
            case "-":
                return val1 - val2
            case "*":
                return val1 * val2
            case "/":
                return int(val1 / val2)
            case _:
                return 0
             