class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A dictionary that maps values to indices
        seen = {}
        
        # Loop through the list. Compute the difference between the target
        # and the current number, searching the dictionary with key = element,
        # value = index. If this exists, you have found the pair and can return.
        # Else, store key = current element, value = index for later computation.
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]
            
            seen[nums[i]] = i