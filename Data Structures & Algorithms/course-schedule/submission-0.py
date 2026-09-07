class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map={i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            pre_map[c].append(pre)
        
        visited=set()
        
        def dfs(c):
            if c in visited: return False
            if pre_map[c]==[]: return True

            visited.add(c)
            for p in pre_map[c]:
                if not dfs(p): return False
            
            visited.remove(c)
            pre_map[c]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True