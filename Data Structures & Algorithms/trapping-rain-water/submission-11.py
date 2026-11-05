class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                area += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                area += rmax - height[r]

        return area