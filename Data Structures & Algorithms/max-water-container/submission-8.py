class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        # Initialize two pointers at the ends to start with the maximum possible width
        l = 0
        r = len(heights) - 1

        while l < r:
            maximum = max(maximum, (r - l) * min(heights[l], heights[r]))
            
            # Move the shorter pointer inwards to see if a larger area is present.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maximum