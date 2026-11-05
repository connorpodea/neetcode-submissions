func twoSum(nums []int, target int) []int {
    diffs := make(map[int]int, len(nums))

    for i, n := range nums {
        diff := target - n
        if idx, ok := diffs[diff]; ok {
            return []int{idx, i}
        }
        diffs[n] = i
    }
    return []int{-1, -1}
}
