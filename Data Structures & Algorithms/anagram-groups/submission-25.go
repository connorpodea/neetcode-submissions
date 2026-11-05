func groupAnagrams(strs []string) [][]string {
    groups := make(map[[26]int][]string)
    var res [][]string

    for _, word := range strs {
        key := [26]int{}

        for _, char := range word {
            key[char - 'a'] += 1
        }

        groups[key] = append(groups[key], word)
    }

    for _, list := range groups {
        res = append(res, list)
    }

    return res
}
