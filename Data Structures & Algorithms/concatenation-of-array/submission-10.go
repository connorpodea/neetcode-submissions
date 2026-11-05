func getConcatenation(nums []int) []int {
    res := make([]int, len(nums)*2)

	for i, n := range nums {
		res[i], res[i + len(nums)] = n, n
	}
	return res
}
