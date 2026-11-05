class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []

        for token in tokens:
            if token not in "+-*/":
                vals.append(int(token))
            else:
                val2 = vals.pop()
                val1 = vals.pop()

                if token == "+":
                    vals.append(val1 + val2)
                elif token == "-":
                    vals.append(val1 - val2)
                elif token == "*":
                    vals.append(val1 * val2)
                else:
                    vals.append(int(val1 / val2))
        return vals.pop()