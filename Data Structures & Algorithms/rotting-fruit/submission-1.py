class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        rotten = []
        fresh = 0
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while rotten and fresh > 0:
            length = len(rotten)
            for i in range(length):
                r, c = rotten.pop(0)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr, nc))

            time += 1
        
        return time if fresh == 0 else -1

