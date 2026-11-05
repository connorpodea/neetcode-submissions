func topKFrequent(nums []int, k int) []int {
    buckets := make([][]int, len(nums) + 1)
    freq := make(map[int]int)
    res := make([]int, 0, k)

    // determine the frequency of each number. key = number in question, value = frequency observed.
    for _, n := range nums {
        freq[n] += 1
    }

    // for each frequency, place it in the proper bucket, where n exists at buckets[n's frequency].
    for n, f := range freq {
        buckets[f] = append(buckets[f], n)
    }

    // reverse search buckets to find the top k elements.
    for i := len(buckets) - 1; i > 0; i -= 1 {
        for _, num := range buckets[i] {
            res = append(res, num)
            
            if len(res) == k {
               return res
            }
        }
    }
    return res
}
