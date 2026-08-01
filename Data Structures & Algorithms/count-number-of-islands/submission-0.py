class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for nr, nc in directions:
                    rownew, colnew = row + nr, col + nc
                    if (rownew in range(rows) and
                    colnew in range(cols) and 
                    (rownew, colnew) not in visited and 
                    grid[rownew][colnew] == "1"):
                        visited.add((rownew, colnew))
                        q.append((rownew,colnew))

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1

        return island 