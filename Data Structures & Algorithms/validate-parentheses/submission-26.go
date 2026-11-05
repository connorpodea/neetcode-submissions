func isValid(s string) bool {
    pair := make(map[rune]rune)
	pair[']'] = '['
	pair['}'] = '{'
	pair[')'] = '('

	stack := []rune{}

	for _, r := range s {
		if r == '[' || r == '{' || r == '(' {
			stack = append(stack, r)
		} else if len(stack) == 0 || pair[r] != stack[len(stack) - 1]{
			return false
		} else {
			stack = stack[:len(stack) - 1]
		}
	}

	return len(stack) == 0
}
