func twoSum(nums []int, target int) []int {
    // create a map to store key: number, value: index
    diffs := make(map[int]int, len(nums))

    // loop through the slice. search for the complementary number in the map
    // if found, return the two indices. else, add this to the map where key = element
    // and value = index
    for i, n := range nums {
        diff := target - n
        if idx, ok := diffs[diff]; ok {
            return []int{idx, i}
        }
        diffs[n] = i
    }
    // a proper match was not found, return an non-successful slice
    return []int{-1, -1}
}
