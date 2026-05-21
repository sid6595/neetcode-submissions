class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrays = []

        for p, s in zip(position, speed):
            arrays.append((p,s))
        
        arrays.sort(reverse=True)
        # [(4,2), (1, 3)]

        stack = []

        for i in range(len(arrays)):
            position = arrays[i][0]
            speed = arrays[i][1]

            # target time = position / speed
            time = (target - position) / speed

            stack.append(time)

            if stack and len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        
        return len(stack)

        