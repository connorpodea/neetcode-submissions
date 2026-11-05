class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = []

        for word in strs:
            mapping = {}

            # create a dict for each char and its frequency
            for i in range(len(word)):
                if word[i] in mapping:
                    mapping[word[i]] += 1
                else:
                    mapping[word[i]] = 1

            # search through previous dictionaries
            # append word to list if found
            # else create a new entry in the seen list
            found = False
            for i in range(len(seen)):
                if seen[i][0] == mapping:
                    seen[i].append(word)
                    found = True
                    break
            if not found:
                seen.append([mapping,word])

        # for each dictionary in seen
        # append the words associated with that dictionary
        # to a slot in the resultant list
        for item in seen:
            res.append(item[1:])
        return res