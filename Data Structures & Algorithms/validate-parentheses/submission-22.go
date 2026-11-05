func isValid(s string) bool {
    stack := []byte{}
    pairs := map[byte]byte {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    for i := 0; i < len(s); i++ {
        b := s[i]

        if b == '{' || b == '(' || b == '[' {
            stack = append(stack, b)
        } else {
            if len(stack) == 0 || pairs[b] != stack[len(stack)-1] {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}