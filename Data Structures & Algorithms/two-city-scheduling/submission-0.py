# minimum cost = dfs
# need to traverse everything

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_people = len(costs)
        city_limit = total_people / 2
        seen = {}

        def dfs(current_p, sent_a):
            if current_p == total_people:
                return 0

            cost_a, cost_b = costs[current_p]
            sent_b = current_p - sent_a

            if (current_p, sent_a) in seen:
                return seen[current_p, sent_a]
            
            res = float('inf')
            
            if sent_a < city_limit:
                res = cost_a + dfs(current_p + 1, sent_a + 1)
            
            if sent_b < city_limit: 
                res = min(res, cost_b + dfs(current_p + 1, sent_a))
            
            seen[current_p, sent_a] = res

            return res

        return dfs(0, 0)

        