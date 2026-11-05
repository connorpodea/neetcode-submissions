func groupAnagrams(strs []string) [][]string {
    groups := make(map[[26]int][]string)
    res := [][]string{}

    for _, word := range strs {
        runeCount := [26]int{}

        for _, char := range word {
            runeCount[char - 'a'] += 1
        }

        groups[runeCount] = append(groups[runeCount], word)
    }

    for _, list := range groups {
        res = append(res, list)
    }

    return res
}
