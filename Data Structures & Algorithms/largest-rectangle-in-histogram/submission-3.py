class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        # appending zero to the end of the list will allow us to compute the final areas.
        heights.append(0) 

        for i in range(len(heights)):
            # If the stack is non-empty and the current height is smaller than the top of
            # the stack, we can no longer extend this rectangle. Compute the area until this
            # point, and update the max area if this is a new max. Doing this for all elements
            # on the stack will allow us to compute all previous rectangles up to this point aswell.
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                height = heights[popped_index]
                width = 0

                # If the stack is now empty, the popped bar is the shortest one seen so far.
                # It can extend all the way back to the very start of the histogram, so the width
                # includes all bars until this point
                if not stack:
                    width = i
                # Otherwise, the new top of the stack is the closest bar to the left that is stictly
                # shorter. This index and 'i' form exclusive boundaries, so the width is the distance
                # between them.
                else:
                    width = i - stack[-1] - 1
                
                area = height * width
                max_area = max(max_area, area)

            # Always append the current element to the top of the stack, since it has the possibility
            # of creating a new max area.
            stack.append(i)
        
        return max_area

