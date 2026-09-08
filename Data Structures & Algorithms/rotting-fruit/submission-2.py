class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n=len(grid), len(grid[0])
        queue=deque([])

        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: fresh+=1
                if grid[i][j]==2: queue.append((i, j, 0))
            
        
        dx=[-1, 0, 1, 0]
        dy=[0, -1, 0, 1]
        time=0
        while queue:
            rotten=queue.popleft()
            time=rotten[2]
            for i in range(4):
                nx=rotten[0]+dx[i]
                ny=rotten[1]+dy[i]
                if nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny]!=1: continue
                grid[nx][ny]=2
                fresh-=1
                queue.append((nx, ny, rotten[2]+1))

        if fresh: return -1
        return time