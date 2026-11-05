func dailyTemperatures(temperatures []int) []int {
	// stack will be in decreasing order
	stack := []int{}
	res := make([]int, len(temperatures))

	for i, n := range temperatures {
		for len(stack) > 0 && n > temperatures[stack[len(stack) - 1]] {
            res[stack[len(stack) - 1]] = i - stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
		}
        stack = append(stack, i)
	}
    return res
}
