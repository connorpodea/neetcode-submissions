type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    res := ""

    // encode the number of strings present
    res += intToStr(len(strs)) + "#"

    // encode the length of each string, as well as the string
    for _, s := range strs {
        // add this to the result string
        res += intToStr(len(s)) + "#" + s
    }

    return res
}

func (s *Solution) Decode(encoded string) []string {
    // extract the number of strings
    numStrings, currIndex := extractLength(encoded, 0)

    res := make([]string, 0, numStrings)

    // extract each remaining string and add it to the result slice
    for currIndex < len(encoded) {
        // extract the number of characters in the current string
        var charCount int
        charCount, currIndex = extractLength(encoded, currIndex)

        // add this word to the result slice and update the index
        res = append(res, encoded[currIndex : currIndex + charCount])
        currIndex += charCount
    }
    return res
}

// converts an integer to a string (helper function to avoid libraries)
func intToStr(n int) string {
    if n == 0 { return "0" }
    res := ""
    for n > 0 {
        res = string(rune(n % 10 + '0')) + res
        n /= 10
    }
    return res
}

// extracts the length from the encoding and updates the index to point after the encoding
func extractLength(str string, startingIndex int) (length, newIndex int) {
    var powerOfTen int

    for i := startingIndex; i < len(str); i += 1 {
        if str[i] == '#' {
            for j := i - 1; j >= startingIndex; j -= 1 {
                length += int(str[j] - '0') * decimalPower(powerOfTen)
                powerOfTen += 1
            }
            newIndex = i + 1
            break
        }
    }
    return length, newIndex
}

// helper function which returns 10^power
func decimalPower(power int) int {
    res := 1
    for i := 0; i < power; i += 1 {
        res *= 10
    }
    return res
}