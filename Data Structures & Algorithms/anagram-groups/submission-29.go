func groupAnagrams(strs []string) [][]string {
	groups := make(map[[26]int][]string)

	for _, s := range strs {
		id := [26]int{}
		for _, r := range s {
			id[r - 'a'] += 1
		}
		groups[id] = append(groups[id], s)
	}

	res := [][]string{}
	for _, v := range groups {
		res = append(res, v)
	}
	return res
}
