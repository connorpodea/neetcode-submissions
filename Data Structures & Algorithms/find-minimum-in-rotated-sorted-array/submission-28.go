func findMin(nums []int) int {
	l, r := 0, len(nums) - 1
	
	// if nums[l] > nums[r], we can look at nums[m] to determine where the min is located at.
	// if nums[m] < nums[l], then the min is located in the left half
	// if nums[m] > nums[l], then the min is located in the right half
	for l < r {
		m := (l + r) / 2

		if nums[m] > nums[r] {
			l = m + 1
		} else {
			r = m
		}
	}
	return nums[l]
}


// [1,2,3,4,5]
// [5,1,2,3,4]
// [4,5,1,2,3]
// [3,4,5,1,2]
// [2,3,4,5,1]
// [1,2,3,4,5]


