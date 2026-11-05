class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit, if the lengths are not equal, they cannot be anagrams.
        if (len(s) != len(t)):
            return False

        # Create a dict for all seen chars, associating the char with its frequency.
        seen = defaultdict(int)
        
        # Increment the frequency of all chars in one of the strings.
        for char in s:
            seen[char] += 1

        # Reverse the previous logic for the other string by decrementing.
        # If the char has a frequency of less than 0, either it never showed up
        # in the original string, or it shows up too many times in the final string.
        for char in t:
            if seen[char] > 0:
                seen[char] -= 1
            else:
                return False
        
        return True
                