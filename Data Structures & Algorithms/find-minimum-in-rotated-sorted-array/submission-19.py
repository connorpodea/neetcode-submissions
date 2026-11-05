class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r: 
            m = (l + r) // 2

            # If the middle element is larger than the right, the
            # smallest element must be in the right half
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the smallest element is at m or to its left
            else: 
                r = m
        # When l == r, both pointers are locked onto the minimum element
        return nums[l]
        