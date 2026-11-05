func search(nums []int, target int) int {
    l, r := 0, len(nums)-1
    res := -1 // 1. Fixed variable declaration

    for l <= r {
        m := l + (r-l)/2 // 2. Fixed midpoint calculation
        currRes := nums[m]

        switch { // 3. Fixed switch syntax
        case currRes < target:
            l = m + 1 // 4. Fixed pointer step
        case currRes > target:
            r = m - 1 // 4. Fixed pointer step
        case currRes == target:
            return m // 5. Return immediately on match
        }
    }
    return res
}