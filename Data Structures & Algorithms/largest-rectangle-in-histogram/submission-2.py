class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                height = heights[popped_index]
                width = 0

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                area = height * width
                max_area = max(max_area, area)

            stack.append(i)
        
        return max_area

