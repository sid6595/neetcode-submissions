class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # is a graph where each node is a coin denomination
        # perform bfs to get to the eventual amount

        # TC: O(V * E)
        # SC: O(V + E)

        if amount == 0:
            return 0
        
        current_count = 1

        queue = deque()
        queue.append(0)
        visited = set()

        while queue:
            print(queue)
            for i in range(len(queue)):
                value = queue.popleft()
                
                for coin in coins:
                    new_value = value + coin
                    if new_value == amount:
                        return current_count
                    if new_value < amount and new_value not in visited:
                        queue.append(new_value)
                        visited.add(new_value)
            
            current_count += 1
        
        return -1