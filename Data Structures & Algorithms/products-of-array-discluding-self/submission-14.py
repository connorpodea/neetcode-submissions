class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1;
        zero_count = 0

        for number in nums:
            if number == 0:
                zero_count += 1
            else: 
                product *= number
        
        for number in nums:
            if zero_count >= 2:
                result = [0] * len(nums)
                break
            elif zero_count > 0 and number != 0:
                result.append(0)
            elif zero_count > 0 and number == 0:
                result.append(product)
            else:
                result.append(int(product / number))
        
        return result