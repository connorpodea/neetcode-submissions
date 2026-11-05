class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = []

        for char in s:
            if char.isalnum():
                formatted.append(char.lower())

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