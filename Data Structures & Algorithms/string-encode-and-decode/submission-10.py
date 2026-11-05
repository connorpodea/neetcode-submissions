class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += f"{len(word):03}" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        index = 0
        while index < len(s):
            string_size = int(s[index:index+3])
            result.append(s[index + 3:index + 3 + string_size]) 
            index += 3 + string_size
        
        return result