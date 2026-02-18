from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        i,j = 0,0
        rows = len(grid)
        cols = len(grid[0])
        fr_or = 0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fr_or += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        tim = 0
        while queue and fr_or > 0:
            
            size = len(queue)
            for _ in range(size):
                x,y = queue.popleft()
                if x + 1 < rows and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    queue.append((x+1,y))
                    fr_or  -=1
                if y + 1 < cols and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    queue.append((x,y+1))
                    fr_or  -=1
                if x - 1 > -1 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    queue.append((x-1,y))
                    fr_or  -=1
                if y - 1 > -1 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    queue.append((x,y-1))
                    fr_or  -=1
            tim += 1
            
        if fr_or == 0:
            return tim
        else:
            return -1

