from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        freq = Counter(nums)  # This gives you a dictionary-like object: {num: count}

        # Step 2: Use a heap to get the k most common elements
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency array of size 2001 to handle -1000 to 1000
        number_freq = [0] * 2001  # index 0 = -1000, index 2000 = 1000

        for number in nums:
            number_freq[number + 1000] += 1

        # List to store top k elements (each as a pair: [number, frequency])
        top_k = []

        for i in range(2001):
            freq = number_freq[i]
            if freq == 0:
                continue

            num = i - 1000  # convert index back to original number

            # Insert this number into the correct position in top_k
            inserted = False
            for j in range(len(top_k)):
                if freq > top_k[j][1]:
                    top_k.insert(j, [num, freq])
                    inserted = True
                    break

            if not inserted and len(top_k) < k:
                top_k.append([num, freq])

            # Trim to size k
            if len(top_k) > k:
                top_k.pop()

        # Extract just the numbers from top_k pairs
        return [pair[0] for pair in top_k]
