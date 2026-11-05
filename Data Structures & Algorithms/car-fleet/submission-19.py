class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # This stack will be used to compute the number of fleets
        cars = [] # This list will concat {position, speed}, and sort it based on position
        count = 1 # The result variable (will always be at least 1).

        # Create our concatonated list
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        # Sort this list based on position, in ascending order.
        cars.sort()
        
        # For each car, compute the time to reach the target, and push it to the stack
        for car in cars:
            time = (target - car[0]) / car[1]
            stack.append(time)

        # The top of the stack contains the car closest to the target. This means any car
        # behind it can finish in the same fleet, or in a later one
        current_fleet_time = stack[-1]

        while stack:
            # If the current top of the stack takes a longer time that the "current fleet",
            # this indicates it belongs to a new fleet. Update the number of fleets, and set
            # the new finish time to compute other possible fleets that end up behind this one.
            if stack[-1] > current_fleet_time:
                count += 1
                current_fleet_time = stack[-1]
            
            # Remove the current vehicle and compute the remaining.
            stack.pop()
        
        return count

