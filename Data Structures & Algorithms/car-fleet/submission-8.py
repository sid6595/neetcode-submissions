# order by position, the start is what matters
# calculate the time to destination - t = d / r
# if the times are lower for a further car push it to the stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_list = list(zip(position, speed))
        car_list.sort(reverse=True)

        stack = []

        for car in car_list:
            position, speed = car
            time = (target - position) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



        