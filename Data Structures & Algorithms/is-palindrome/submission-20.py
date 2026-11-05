class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = []

        # Create a new string that formats the string into lowercase
        # characters without whitespace or punctuation.
        for char in s:
            if char.isalnum():
                formatted.append(char.lower())

        # Create a left and right pointer, moving from the outside of 
        # the string to the middle, checking if the character at the
        # left index match the character at the right index.
        l = 0
        r = len(formatted) - 1

        while l < r:
            lchar = formatted[l]
            rchar = formatted[r]

            if lchar != rchar:
                return False
            else:
                l += 1
                r -= 1
        
        return True