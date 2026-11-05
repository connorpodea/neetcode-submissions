func largestRectangleArea(heights []int) int {
	// Make a copy and append 0 at the end to trigger remaining calculations
	// (Avoids mutating the caller's slice directly)
	h := make([]int, len(heights), len(heights)+1)
	copy(h, heights)
	h = append(h, 0)

	stack := make([]int, 0)
	maxArea := 0

	for i := 0; i < len(h); i++ {
		// While stack is non-empty and current height is smaller than top of stack
		for len(stack) > 0 && h[i] < h[stack[len(stack)-1]] {
			// Pop from stack
			poppedIndex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			height := h[poppedIndex]
			var width int

			if len(stack) == 0 {
				width = i
			} else {
				width = i - stack[len(stack)-1] - 1
			}

			area := height * width
			maxArea = max(maxArea, area)
		}

		// Push current index to stack
		stack = append(stack, i)
	}

	return maxArea
}