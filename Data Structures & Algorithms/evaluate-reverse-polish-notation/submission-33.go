func evalRPN(tokens []string) int {
	stack := []int{}

	for _, s := range tokens {
		if s == "+" || s == "-" || s == "*" || s == "/" {
			val1 := stack[len(stack) - 2]
			val2 := stack[len(stack) - 1]
			stack = stack[:len(stack) - 2]

			switch s {
				case "+":
					stack = append(stack, val1 + val2)
				case "-":
					stack = append(stack, val1 - val2)
				case "*":
					stack = append(stack, val1 * val2)
				case "/":
					stack = append(stack, val1 / val2)
			}
		} else {
			stack = append(stack, strToInt(s))
		}
	}
	return stack[0]
}

func strToInt(s string) int {
    if len(s) == 0 {
        return 0
    }

    sign := 1
    startIndex := 0

    // 1. Check for a negative (or positive) sign
    if s[0] == '-' {
        sign = -1
        startIndex = 1 // Start reading numbers *after* the minus sign
    } else if s[0] == '+' {
        startIndex = 1 // Start reading numbers *after* the plus sign
    }

    res := 0
    // 2. Loop through the remaining characters
    for i := startIndex; i < len(s); i++ {
        // Convert the byte character to its actual numeric value
        digit := int(s[i] - '0')
        
        // Build the number place-by-place
        res = (res * 10) + digit
    }

    // 3. Apply the sign and return
    return res * sign
}