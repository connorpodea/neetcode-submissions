class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            identifier = [0] * 26

            for char in word:
                identifier[ord(char) - ord('a')] += 1
            
            res[tuple(identifier)].append(word)
    
        return list(res.values())

