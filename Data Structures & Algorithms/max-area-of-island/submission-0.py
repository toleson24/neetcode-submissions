class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def bfs(x, y):
            queue = [(x, y)]
            area = 1
            grid[x][y] = 0
            
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 > nx or nx >= len(grid) or 0 > ny or ny >= len(grid[0]) or grid[nx][ny] == 0:
                        continue

                    queue.append((nx, ny))
                
                    area += 1
                    grid[nx][ny] = 0

            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))

        return max_area

        