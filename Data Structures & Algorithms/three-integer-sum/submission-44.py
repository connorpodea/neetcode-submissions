class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                triplet_sum = nums[i] + nums[l] + nums[r]

                if triplet_sum < 0:
                    l += 1
                elif triplet_sum > 0:
                    r -= 1
                elif triplet_sum == 0:
                    res.append(triplet)
                    
                    # skip duplicates for left pointer
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # skip duplicates for right pointer
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # move to the next unique pair
                    l += 1
                    r -= 1
            
        return res