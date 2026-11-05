class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # If we find the target, return the index immediately.
            if nums[m] == target:
                return m
            
            # In a rotated sorted array, one side will be perfectly
            # sorted. Check to see which side is sorted before continuing.

            # Case 1: The left half of the array is normally sorted.
            if nums[l] <= nums[m]:
                # Check if the target lies within this sorted half.
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Case 2: The right half of the array is normally sorted.
            else:
                # Check if the target lies within this sorted half.
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1