class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums) # Create a set for cheap lookups.
        longest = 0 # Result

        for num in nums:
            curr_sequence = 1

            # Check if this number is the start of a unique sequence by checking
            # if its predecessor exits, and if not, looping through its successors
            # checking if they exist, creating a counter for each sequence.
            if num - 1 not in set_nums:
                while (num + 1 in set_nums):
                    curr_sequence += 1
                    num += 1
            longest = max(longest, curr_sequence)
        
        return longest