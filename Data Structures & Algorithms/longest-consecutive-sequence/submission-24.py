class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in nums:
            curr_sequence = 1
            if num - 1 not in set_nums:
                while (num + 1 in set_nums):
                    curr_sequence += 1
                    num += 1
            longest = max(longest, curr_sequence)
        
        return longest