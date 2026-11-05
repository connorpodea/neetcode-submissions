class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0

        for number in nums:
            if number:
                prod *= number
            else: 
                zero_count += 1
        
        if zero_count > 1: 
            return [0] * len(nums)

        result = []
        for number in nums:
            if zero_count == 1 and number:
                result.append(0)
            elif zero_count == 1 and not number:
                result.append(prod)
            else:
                result.append(prod // number)
        
        return result