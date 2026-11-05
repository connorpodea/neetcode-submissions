func isPalindrome(s string) bool {
	l := 0
	r := len(s) - 1

	for l < r {
		lbyte := s[l]
		rbyte := s[r]

		if !isAlnum(lbyte) {
			l += 1
			continue
		}
		if !isAlnum(rbyte) {
			r -= 1
			continue
		}

		if toLower(lbyte) != toLower(rbyte) {
			return false
		}
		l += 1
		r -= 1
	}
	return true
}

func isAlnum(b byte) bool {
	res := (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
	return res
}

func toLower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + ('a' - 'A')
	}
	return b
}
