class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inbound=[0]*numCourses

        pre_map={i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            inbound[c]+=1
            pre_map[p].append(c)
        
        completed=0
        queue=deque([])
        for i in range(numCourses):
            if inbound[i]==0: queue.append(i)
        
        while queue:
            v=queue.popleft()
            completed+=1
            for nbr in pre_map[v]:
                inbound[nbr]-=1
                if inbound[nbr]==0:
                    queue.append(nbr)
        
        return completed==numCourses

