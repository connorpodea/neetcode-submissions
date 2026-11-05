class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        seen = defaultdict(int)
        
        for char in s:
            seen[char] += 1

        for char in t:
            if seen[char] > 0:
                seen[char] -= 1
            else:
                return False
        
        return True
                