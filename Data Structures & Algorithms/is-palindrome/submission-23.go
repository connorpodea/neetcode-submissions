func isPalindrome(s string) bool {
	l, r := 0, len(s) - 1

    for l <= r {
        lb, rb := s[l], s[r]

        if !isAlphaNum(lb) {
            l += 1
            continue
        }
        if !isAlphaNum(rb) {
            r -= 1
            continue
        }

        if toLower(lb) != toLower(rb) {
            return false
        }
        l += 1
        r -= 1
    }
    return true
}

func isAlphaNum(b byte) bool {
    return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
}

func toLower(b byte) byte {
    if b >= 'A' && b <= 'Z' {
        return b + 32
    }
    return b
}
