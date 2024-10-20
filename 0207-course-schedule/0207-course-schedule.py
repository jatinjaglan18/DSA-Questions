class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisitesMap = {i:[] for i in range(numCourses)}

        for currentCourse, prerequisite in prerequisites:
            prerequisitesMap[currentCourse].append(prerequisite)
        
        visited = set()
        def dfs(currentCourse):

            if currentCourse in visited:
                return False

            if prerequisitesMap[currentCourse] == []:
                return True
            
            visited.add(currentCourse)
            for course in prerequisitesMap[currentCourse]:
                if not dfs(course):
                    return False
            
            visited.remove(currentCourse)
            prerequisitesMap[currentCourse] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
           
        
        