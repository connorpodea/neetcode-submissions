class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Pre-allocate the list with 0s to avoid IndexErrors
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # 2. Pop elements from the stack while the current day is warmer
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            # 3. Always push the current day's index onto the stack
            stack.append(i)
        
        # Because 'res' was initialized with 0s, any index left in 
        # the stack automatically stays 0. No extra loop needed!
        return res