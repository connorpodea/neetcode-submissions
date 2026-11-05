class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += f"{len(word):03}" + word
        
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            word_length = int(s[i:i + 3])
            result.append(s[i + 3:i + 3 + word_length])
            i += 3 + word_length
        
        return result

