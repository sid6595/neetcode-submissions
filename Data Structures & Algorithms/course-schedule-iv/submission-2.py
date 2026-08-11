# input
# numCourses = int : 0 -> numCourses - 1 total courses
# prerequisites || [[ai, bi], [a2, b2], ...] || course a required for course b
# queries || [[uj, vj], [u2, v2], ...] || want to check whether we need course u for course v

# output
# res || [true, true, ...] || we check each item in queries

# create sets for each course that contains all its prereqs
# if prereq in queries[j] return true else false

# directed graph, prereqs are our edges
# a -> b -> c
#        -> d
# 

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjList = defaultdict(list)

        for prereq, source in prerequisites:
            adjList[source].append(prereq)
        

        prereq_dict = defaultdict(set)

        def dfs(node):
            # post order traversal: visit our connected components first
            if node in prereq_dict:
                return prereq_dict[node]

            res = set()

            for p in adjList[node]:
                res.add(p)
                res.update(dfs(p))
            
            prereq_dict[node] = res
            return res

        # populate our prereq dictionary
        # only look at courses we haven't visited yet
        # O(V + E)
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for query in queries:
            res.append(True) if query[0] in prereq_dict[query[1]] else res.append(False)
        
        return res
                


        