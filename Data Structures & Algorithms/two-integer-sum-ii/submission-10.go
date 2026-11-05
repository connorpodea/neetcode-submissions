func twoSum(numbers []int, target int) []int {
    indxMap := make(map[int]int)

    for i, n := range numbers {
        diff := target - n

        if indxMap[diff] != 0 {
            return []int{indxMap[diff], i + 1}
        }
        indxMap[n] = i + 1
    }
    return []int{-1,-1}
}
