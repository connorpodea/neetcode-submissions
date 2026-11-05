func isAnagram(s string, t string) bool {
    if len([]rune(s)) != len([]rune(t)) {
        return false
    }

    seen := make(map[rune]int)

    for _, char := range s {
        seen[char] += 1
    }

    for _, char := range t {
        if count := seen[char]; count < 1 {
            return false
        }
        seen[char] -= 1
    }

    return true
}
