func getConcatenation(nums []int) []int {
	res := make([]int, 2*len(nums))

	for i, n := range nums {
		res[i], res[i + len(nums)] = n, n
	}
	return res
}
