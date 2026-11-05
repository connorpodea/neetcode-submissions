class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                res.append(seen[difference])
                res.append(i)
            
            else:
                seen[nums[i]] = i

        return res