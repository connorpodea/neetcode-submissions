class Solution:

    def encode(self, strs: List[str]) -> str:
        # The list that will be passed to decode
        res = []
        
        # Since the number of lists <= 100, 3 digits are needed to encode the number of lists.
        res.append(str(len(strs)).zfill(3))

        # Loop through each word in the list. First, encode the number of chars in the word, followed
        # by the actual word. Once all words are encoded, join the result list into a string and pass
        # it to decode.
        for word in strs:
            # Since the char count of any list <= 200, 3 digits are needed to encode the char count 
            # of each list.
            res.append(str(len(word)).zfill(3))
            for char in word:
                res.append(char)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # The number of words are stored in the first 3 char, extract these to set a proper loop.
        num_lists = int(s[0:3])

        # Create an empty nested list using our extracted number of lists.
        res = [[] for _ in range(num_lists)]

        # Start looping through the string, starting after the previously extracted portion.
        curr_index = 3
    
        for i in range(num_lists):
            # Extract the length of the current word using our offset of what has been computed.
            word_length = int(s[curr_index : curr_index + 3])
            curr_index += 3

            # Append the word to the returned list and update the offset to extract the next word.
            res[i] = s[curr_index : curr_index + word_length]
            curr_index += word_length

        return res