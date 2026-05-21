# input: int telling us how many nodes, list of edges
# output: nodes which gives us the MHT

# we don't need to create a new tree at every possible node and get height
# O (n) * O(n) = O(n^2)

# instead we can create one tree
# calculate the longest path from that node to another node
# that is that node's nht
# O (n) + n * O(n) = O(n)
# SC: O(n)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create the graph
        # adjacency list

        adj_list = defaultdict(list)

        # connect all nodes with edges
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        
        # traverse graph from each point
        def bfs(node):
            queue = deque()
            visited = set()

            queue.append(node)
            length = 0

            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    visited.add(node)
                    for neighbor in adj_list[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                length += 1
            
            return length

        res = defaultdict(list)
        min_seen = 2000000
        
        for i in range(n):
            min_seen = min(min_seen, bfs(i))
            res[bfs(i)].append(i)
        
        return res[min_seen]
            
        
        