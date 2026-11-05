func longestConsecutive(nums []int) int {
	set := make(map[int]bool)
    longest := 0


    for _, n := range nums {
        set[n] = true
    }

    for n := range set {
        currSeq := 1
    
        if !set[n - 1] {
            for set[n + 1] {
                currSeq += 1
                n += 1
            }
        }
        if currSeq > longest {
            longest = currSeq
        }
    }
    return longest
}
