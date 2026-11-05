class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = {}

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key not in anagram_list:
                anagram_list[key] = []
            anagram_list[key].append(word)

        result = []

        return list(anagram_list.values())

        
