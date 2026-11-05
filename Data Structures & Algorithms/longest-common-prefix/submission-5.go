func longestCommonPrefix(strs []string) string {
    res := ""
	index := 0
	var currByte byte

	for index >= 0 {
		for i, s := range strs {
			if i == 0 && index < len(s) {
				currByte = s[index]
			}
			if index >= len(s) || s[index] != currByte {
				return res
			}
		}
		res += string(currByte)
		index += 1
	}
	return res
}
