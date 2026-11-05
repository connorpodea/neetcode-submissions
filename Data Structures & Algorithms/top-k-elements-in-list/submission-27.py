class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [0] * 2001
        freq_rank = [[] for _ in range(2001)]

        # compute the frequency of each number
        # index offset of 1000
        for num in nums:
            freq[num + 1000] += 1
        
        # for each num, store the num at the index given by its freq
        for i in range(len(freq)):
            freq_rank[freq[i]].append(i - 1000)


        for i in range(len(freq_rank) - 1, 0, -1):
            for num in freq_rank[i]:
                res.append(num)
            
            if (len(res) >= k):
                break

        return res
