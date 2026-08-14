# input: deadend strings, target string
# output: starting from '0000', minimum moves to reach target string

# key info
# if we are ever displaying a deadend string, we lose
# in python, we don't need to do int conversion if we're comparing one char

# questions
# will we ever have invalid inputs? -> no
# what is the largest length of deadends? -> 500
# will there always be a valid solution? -> no, return -1
# can the target ever be in the deadends list? -> no

# examples
# deadends = ["1111","0120","2020","3333"], target = "5555"
# start at 0000
# 5 turns: 5000
# 20 total

# approach
# turn this into a graph
# 0000 -> root node
# each node can have 4 neighbors -> 1000, 0100, 0010, 0001
# then, we run some exploration down the tree -> minimum path -> BFS
# we stop exploring a route if we ever hit a deadend or we can't reach our target
# stop when we reach our required node combination
# level order traversal



class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"

        i_deadends = set(deadends)

        if start in i_deadends:
            return -1

        if start == target:
            return 0

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        res = 0

        while queue:
            # level order traversal
            # let's us get our minimum path
            for i in range(len(queue)):
                # i doesn't matter
                # 0000, 1000, ... 
                cur = queue.popleft() # int
                
                if cur == target:
                    return res
                
                for child in children(cur):
                    #generate 8 neighbors
                    if child not in visited and child not in i_deadends:
                        visited.add(child)
                        queue.append(child)
                              
            res += 1
        
        return -1



        