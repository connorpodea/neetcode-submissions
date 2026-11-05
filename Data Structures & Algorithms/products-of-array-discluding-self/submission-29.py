class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Important to track the number of zeroes
        zero_count = 0
        total_product = 1
        res = []

        # Loop through each number, keeping track of the number of zeroes as well as the total product
        for num in nums:
            if num == 0:
                zero_count += 1
            else: 
                total_product *= num

        # More than 1 zero will mean all resulting elements are 0. Can quick return.
        if zero_count > 1:
            return [0] * len(nums)
        
        # Loop through all elements. If there are no zeroes, simply divide the total product by the 
        # current number, assigning that number to the resultant array.If 1 zero exists, the product 
        # for all elements besides the zero will be 0. At the index of the zero, the product will be
        # equal to the total product. 
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(total_product)
            elif zero_count == 1:
                res.append(0)
            else:
                res.append(total_product // nums[i])

        return res

        