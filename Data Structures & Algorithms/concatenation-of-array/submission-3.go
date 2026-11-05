func getConcatenation(nums []int) []int {
    for _, n := range nums {
		nums = append(nums, n)
	}
	return nums
}
