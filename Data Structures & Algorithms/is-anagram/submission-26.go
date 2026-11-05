func isAnagram(s string, t string) bool {
    // this is assuming that characters are ascii
    // if the number of runes differ, they cannot be anagrams
    if len(s) != len(t) {
        return false
    }

    // create a map to store the net count of each rune
    seen := make(map[rune]int)

    // loop through s, incrementing the occurence of each rune
    for _, char := range s {
        seen[char] += 1
    }

    // loop through t, decrementing the occurence of each rune if possible
    // if decrementing is not possible without going negative, they cannot be anagrams
    for _, char := range t {
        if count := seen[char]; count < 1 {
            return false
        }
        seen[char] -= 1
    }

    // if all runes are accounted for and program has not exited until this point, the
    // two strings are anagrams
    return true
}
