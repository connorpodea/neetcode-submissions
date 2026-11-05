class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_product = 1
        res = []

        for num in nums:
            if num == 0:
                zero_count += 1
            else: 
                total_product *= num

        if zero_count > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(total_product)
            elif zero_count == 1:
                res.append(0)
            else:
                res.append(total_product // nums[i])

        return res

        