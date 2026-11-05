func longestCommonPrefix(strs []string) string {
    res := ""
	index := 0
	
	for {
        var currByte byte
		
        for i, s := range strs {
            if index >= len(s) {
                return res
            }

            if i == 0 {
                currByte = s[index]
            } else if s[index] != currByte {
                return res
            }
        }
        res += string(currByte)
        index += 1
	}
	return res
}
