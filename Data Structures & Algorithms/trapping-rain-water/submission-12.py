class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        
        # Start two pointers at both ends of the arrays.
        l = 0
        r = len(height) - 1
        
        # Track the highest boundary wall seen so far from the left and from the right.
        lmax = height[l]
        rmax = height[r]

        while l < r:
            # The water level above any bar is limited by the shorter of its surrounding walls: min(lmax, rmax).
            # If lmax is strictly smaller than rmax, then lmax is the definitive bottleneck for the left side.
            # We don't care what's in the middle because 'rmax' acts as a giant right-side barrier ensuring 
            # water won't spill out. Therefore, we can safely step the left pointer forward.
            if lmax < rmax:
                l += 1
                # Update our highest left wall if the new bar is taller.
                lmax = max(lmax, height[l])
                # The trapped water above this single bar is the current wall height minus the bar's own height.
                area += lmax - height[l]
            
            # If rmax is smaller than or equal to lmax, then rmax is the bottleneck for the right side.
            # 'lmax' acts as the giant left-side barrier, so we can safely step the right pointer inward.
            else:
                r -= 1
                # Update our highest right wall if the new bar is taller.
                rmax = max(rmax, height[r])
                # The trapped water above this single bar is the current wall height minus the bar's own height.
                area += rmax - height[r]

        return area