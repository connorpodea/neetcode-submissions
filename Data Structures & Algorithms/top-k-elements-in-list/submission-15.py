class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_freq = [0] * 2001  # Handle numbers from -1000 to 1000

        for number in nums:
            number_freq[number + 1000] += 1

        top_k = []  # List of tuples: (num, frequency)

        for i in range(2001):
            freq = number_freq[i]
            if freq == 0:
                continue

            num = i - 1000  # Convert index back to actual number
            inserted = False

            for j in range(len(top_k)):
                if freq > top_k[j][1]:  # Compare frequencies
                    top_k.insert(j, (num, freq))  # Insert as a tuple
                    inserted = True
                    break

            if not inserted and len(top_k) < k:
                top_k.append((num, freq))

            if len(top_k) > k:
                top_k.pop()

        return [pair[0] for pair in top_k]  # Extract just the numbers
