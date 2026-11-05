class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Count the frequency of each number.
        for num in nums:
            freqs[num] += 1

        # For each frequency, store the numbers associated.
        for key, val in freqs.items():
            buckets[val].append(key)
        
        # For the highest frequencies, append the numbers associated
        # to the returning list
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res