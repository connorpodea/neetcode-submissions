class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []
        
        # since the number of lists <= 100, 3 digits
        # are needed to encode the number of lists
        res.append(str(len(strs)).zfill(3))

        for word in strs:
            # since the char count of any list <= 200, 3 digits
            # are needed to encode the char count of each list
            res.append(str(len(word)).zfill(3))
            for char in word:
                res.append(char)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        num_lists = int(s[0:3])

        res = [[] for _ in range(num_lists)]

        curr_index = 3
    
        for i in range(num_lists):
            word_length = int(s[curr_index : curr_index + 3])
            curr_index += 3

            res[i] = s[curr_index : curr_index + word_length]
            curr_index += word_length

        return res