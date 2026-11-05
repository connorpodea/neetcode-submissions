class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1

        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                if lmax < height[l]:
                    lmax = height[l]
                else:
                    area += lmax - height[l]
                    l += 1
            else:
                if rmax < height[r]:
                    rmax = height[r]
                else:
                    area += rmax - height[r]
                    r -= 1

        return area