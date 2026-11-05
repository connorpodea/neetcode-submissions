class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # This stack will contain temperatures in descending order.
        res = [0] * len(temperatures) # Our result list initialized with zero (helpful when no later days have a higher temp).

        # Loop through the temperates
        for i in range(len(temperatures)):
            # If previous elements are in the stack, and the current temperature is greater than the top of the stack, this means 
            # we can update the result list. Loop through the stack to update the days with a lower temperature than the current days
            # temperature, and pop that element from the stack since we have computed its result.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()    
            # Always append the current day, since we have not yet found a later day with a higher temperature.
            stack.append(i)
            
        return res
