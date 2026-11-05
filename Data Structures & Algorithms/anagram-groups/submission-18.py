class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = []

        for word in strs:
            mapping = defaultdict(int)

            # Create a dict for each char and its frequency.
            for i in range(len(word)):
                mapping[word[i]] += 1

            # Search through previous dictionary entries. Append word to
            # list if found, else create a new entry in the seen list.
            found = False
            for i in range(len(seen)):
                if seen[i][0] == mapping:
                    seen[i].append(word)
                    found = True
                    break
            if not found:
                seen.append([mapping,word])

        # For each dictionary in seen, append the words associated 
        # with that dictionary to a slot in the resultant list.
        for item in seen:
            res.append(item[1:])
        return res