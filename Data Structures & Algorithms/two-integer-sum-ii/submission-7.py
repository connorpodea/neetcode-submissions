class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at opposite ends of the sorted array.
        l = 0
        r = len(numbers) - 1

        while l < r:
            lnum = numbers[l]
            rnum = numbers[r]
            
            # Since the array is sorted, if the current sum is too small,
            # we must move the left pointer right to get a larger value.
            if lnum + rnum < target:
                l += 1
            # If the current sum is too large, we must move the right pointer
            # left to get a smaller value.
            elif lnum + rnum > target:
                r -= 1
            # If the sum perfectly matches the target, stop searching.
            else:
                break

        # Convert to a 1-index positions.
        return [l + 1, r + 1]