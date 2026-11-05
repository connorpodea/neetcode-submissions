func longestConsecutive(nums []int) int {
	set := make(map[int]bool)
    res := 0

    for _, n := range nums {
        set[n] = true
    }

    for n := range set {
        if !set[n - 1] {
            currSeq := 1
            for set[n + 1] {
                currSeq += 1
                n += 1
            }
            res = max(res, currSeq)
        }
    }
    return res
}
