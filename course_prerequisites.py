from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i : list() for i in range(numCourses)}
        visited = [False] * numCourses
        rec_stack = [False] * numCourses
        for p in prerequisites:
            edges[p[0]].append(p[1])
        
        def is_cyclic(v):
            visited[v] = True
            rec_stack[v] = True
            for neighbour in edges[v]:
                if not visited[neighbour]: 
                    if is_cyclic(neighbour): 
                        return True
                elif rec_stack[neighbour]:
                    return True
            rec_stack[v] = False
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if is_cyclic(i):
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    n = 2
    prerequisites = [[1,0]]
    print(sol.canFinish(n, prerequisites))
    prerequisites = [[1,0],[0,1]]
    print(sol.canFinish(n, prerequisites))