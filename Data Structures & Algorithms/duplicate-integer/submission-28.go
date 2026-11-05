func hasDuplicate(nums []int) bool {
    visited := make(map[int]struct{})

    for _, n := range nums {
        if _, exists := visited[n]; exists {
            return true
        }
        visited[n] = struct{}{}
    }
    return false
}
