class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        index = 0

        while True:
            curr_char = ''
            for i in range(len(strs)):
                if index >= len(strs[i]):
                    return res
                
                if i == 0:
                    curr_char = strs[i][index]
                elif strs[i][index] != curr_char:
                    return res
            res += curr_char
            index += 1
        
        return res