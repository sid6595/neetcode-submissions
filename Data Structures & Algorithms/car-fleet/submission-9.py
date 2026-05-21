class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # order cars by position
        car_fleet = list(zip(position,speed))
        # sort from greatest position to least (closest to target first)
        car_fleet.sort(key=lambda x: x[0], reverse=True)

        # iterate through the cars and calculate their time to target
        # if a time is greater than the previous, add it to the stack, add it to the total
        fleet_count = 1
        stack = [(target - car_fleet[0][0]) / car_fleet[0][1]]

        for i in range(1, len(car_fleet)):
            time_to_target = (target - car_fleet[i][0]) / car_fleet[i][1]

            if time_to_target > stack[-1]:
                stack.append(time_to_target)
                fleet_count += 1
        
        return fleet_count




