# given: prerequisites -> array -> prerequisites[i] = [a,b], num courses to take
# output: bool -> is it possible to finish all courses

# key info
# prerequisites elements will always be length 2

# approach

# create a directed graph
# adjacency list, stored as a hashmap
# 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
        
        course_reqs = {i: [] for i in range(numCourses)}
        # create our adjacency list with each course and its requirements
        for pair in prerequisites: 
            second_class, first_class = pair
            course_reqs[second_class].append(first_class)
        
        # now we know what classes we need to take before we attend the one we're looking at
        
        # dfs through the graph we've created
        # if we can traverse through every neighbor, we can complete our class
        # do this for every class
        # if we can return true
        # if we fail at any point, return false

        # algebra 3: [algebra 1, algebra 2]
        # algebra 2: [algebra 1]
        # algebra 1: []

        def dfs(adjacency_list, initial_course, visited):
            if initial_course in visited:
                return True
            if initial_course in visiting:
                return False
            
            visiting.add(initial_course)
            for nei in course_reqs[initial_course]:
                if not dfs(adjacency_list, nei, visited):
                    return False
            visiting.remove(initial_course)
            
            visited.add(initial_course)
            return True
        
        for i in range(numCourses):
            if not dfs(course_reqs, i, visited):
                return False
        
        return True
        


        