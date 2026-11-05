from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        freq = Counter(nums)  # This gives you a dictionary-like object: {num: count}

        # Step 2: Use a heap to get the k most common elements
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
