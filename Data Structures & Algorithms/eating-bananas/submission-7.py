class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko is bounded by 2 logical speeds :
        # Min: 1 / hr
        # Max : size of largest pile / hr

        # Instead of trying each possible speed (from min to max)
        # We can perform a "binary search" on the optimal speed
        # This results in n accesses log(m) times, or O(nlog(m))

        smallest, largest = 1, 0

        # Find the largest pile
        for count in piles:
            if count > largest:
                largest = count

        l, r = smallest, largest
        k = largest

        # Begin searching for the minimum speed
        while l <= r:
            speed = (l + r) // 2
            hrs = 0
            
            for pile_size in piles:
                hrs += math.ceil(pile_size / speed)

            # If the current time < h AND the speed is less than k
            # Update k = speed
            if hrs <= h and speed < k:
                k = speed
            
            # if the time is less than our restriction, we can try a slower speed
            if hrs <= h:
                r = speed - 1
            # if the time is greater than our restriction, we MUST try a higher speed
            elif hrs > h:
                l = speed + 1
            
        return k

            
