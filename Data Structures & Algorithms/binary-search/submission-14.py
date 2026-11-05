class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the boundaries.
        l = 0
        r = len(nums) - 1

        # Start the search.
        while (l <= r):
            # Compute the middle element.
            m = (l + r) // 2

            # If the current element is less than the target, update the left bound
            # If the current element is greater than the target, update the right bound
            # Otherwise, we have foudn the target, and can return the index.
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        # Return -1 if the element is not found in the list.
        return -1
