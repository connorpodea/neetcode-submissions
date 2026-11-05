func isAnagram(s string, t string) bool {
	count := make(map[rune]int)

	if len(s) != len(t) {
		return false
	}

	for _, c := range s {
		count[c] += 1
	}

	for _, c := range t {
		if count[c] <= 0 {
			return false
		}
		count[c] -= 1
	}
	return true
}
