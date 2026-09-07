class Solution:
    def explore(self, grid: List[List[str]], i: int, j: int, n: int, m: int) -> None:
        if i<0 or i>=n or j<0 or j>=m or grid[i][j]!="1": return

        grid[i][j] = "0"
        self.explore(grid, i-1, j, n, m)
        self.explore(grid, i, j-1, n, m)
        self.explore(grid, i+1, j, n, m)
        self.explore(grid, i, j+1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        noi = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.explore(grid, i, j, n, m)
                    noi+=1
        
        return noi