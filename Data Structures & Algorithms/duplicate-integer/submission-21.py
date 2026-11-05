class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sets remove duplicate elements. If the size of the original
        # input is not the same as the input's set, there exists a duplicate.
        return(len(nums) != len(set(nums)))