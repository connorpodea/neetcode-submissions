func hasDuplicate(nums []int) bool {
    set := make(map[int]bool, len(nums))

	for _, n := range nums {
		if set[n] == true {
			return true
		}
		set[n] = true
	}
	return false
}
