func longestCommonPrefix(strs []string) string {
    res := ""
	index := 0
	var currRune rune

	for index >= 0 {
		for i, s := range strs {
			if i == 0 && index < len(s) {
				currRune = rune(s[index])
			}
			if index >= len(s) || rune(s[index]) != currRune {
				return res
			}
		}
		res += string(currRune)
		index += 1
	}
	return res
}
