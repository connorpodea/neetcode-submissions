class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d= {}
        for i in range(len(nums)):
            n1= nums[i]
            n2= target- n1
            if n2 in d:
                return [d[n2], i]
            d[n1]=i