class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = []
        visiting = set()
        
        course_reqs = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            course_reqs[course].append(prereq)

        # now have a dictionary containing all class and their prereq

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for neighbor in course_reqs[course]:
                if not dfs(neighbor):
                    return False
            
            visiting.remove(course)

            visited.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return visited

