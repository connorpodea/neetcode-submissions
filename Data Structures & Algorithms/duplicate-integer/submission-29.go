func hasDuplicate(nums []int) bool {
    // create a map to identify visited numbers (using structs as values since they're 'free')
    visited := make(map[int]struct{})

    // loop through each element in the slice
    for _, n := range nums {
        // check if this element is in the map, if so return true
        if _, exists := visited[n]; exists {
            return true
        }
        // always add this element to the map
        visited[n] = struct{}{}
    }
    // the loop has completed without returning, meaning all elements are unique
    return false
}
