class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # We stop at len(nums) - 2 because a triplet requires at least two more elements after 'i'.
        for i in range(len(nums) - 2):
            # If the current number is the same as the previous one, skip it.
            # This prevents us from generating duplicate triplets starting with the same value.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Use the two pointer approach for the remaining part of the array.
            l = i + 1
            r = len(nums) - 1
            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                triplet_sum = nums[i] + nums[l] + nums[r]

                # If the sum is too small, move the left pointer right to get a larger value.
                if triplet_sum < 0:
                    l += 1
                # If the sum is too large, move the right pointer left to get a smaller value.
                elif triplet_sum > 0:
                    r -= 1
                # Found a valid triplet that sums to zero
                elif triplet_sum == 0:
                    res.append(triplet)
                    
                    # To avoid duplicate triplets from the inner loop, skip over any 
                    # identical numbers next to our current left and right pointers.
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # Move both pointers inward to begin searching for the next unique pair
                    l += 1
                    r -= 1
            
        return res