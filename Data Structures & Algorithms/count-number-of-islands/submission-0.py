class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = ((0, 1), (1, 0), (0, -1), (-1, 0))

        islands = 0
        
        def dfs(x, y):
            if 0 > x or x >= len(grid) or 0 > y or y >= len(grid[0]) or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            for nx, ny in adj:
                dfs(x + nx, y + ny)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        
        return islands
