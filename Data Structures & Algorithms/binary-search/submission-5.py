class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l <= r):
            m = (r - l) // 2 + l
            curr = nums[m]

            if curr < target:
                l = m + 1
            elif curr > target:
                r = m - 1
            else:
                return m
        
        return -1
