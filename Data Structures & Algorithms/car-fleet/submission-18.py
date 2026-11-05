class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        count = 1

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort()

        for car in cars:
            time = (target - car[0]) / car[1]
            stack.append(time)

        current_fleet_time = stack[-1]

        while stack:
            if stack[-1] > current_fleet_time:
                count += 1
                current_fleet_time = stack[-1]
            
            stack.pop()
        
        return count

