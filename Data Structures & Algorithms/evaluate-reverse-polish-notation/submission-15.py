class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        vals = []

        for token in tokens:
            if token in ops :
                val2 = vals.pop()
                val1 = vals.pop()
                vals.append(self.compute(token, val1, val2))
                continue
            vals.append(int(token))

        return vals[0]

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
             