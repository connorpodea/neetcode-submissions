class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                result += lMax - height[l]
            else: 
                r -= 1
                rMax = max(rMax, height[r])
                result += rMax - height[r]
                
        
        return result
