func search(nums []int, target int) int {
    l, r := 0, len(nums)-1
    res := -1

    for l <= r {
        m := l + (r-l) / 2
        currRes := nums[m]

        switch {
        case currRes < target:
            l = m + 1
        case currRes > target:
            r = m - 1
        case currRes == target:
            return m
        }
    }
    return res
}