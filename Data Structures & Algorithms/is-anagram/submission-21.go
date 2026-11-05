func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    seen := make(map[rune]int)

    for _, char := range s {
        seen[char] += 1
    }

    for _, char := range t {
        count := seen[char]
        if count < 1 {
            return false
        }
        seen[char] -= 1
    }

    return true
}
