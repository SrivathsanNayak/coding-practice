class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def bfs(r, c):
            #queue
            q = collections.deque()
            #mark as visited
            visit.add((r, c))
            q.append((r, c))
            
            #while queue not empty
            while q:
                row, col = q.popleft()
                #top, right, bottom, left
                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                
                for dr, dc in directions:
                    #moving to adjacent cells
                    nr, nc = row + dr, col + dc
                    
                    #check if land in bounds
                    if ((0 <= nr < len(grid)) and (0 <= nc < len(grid[0]))
                        and (grid[nr][nc] == "1") and ((nr, nc) not in visit)):
                        #mark land visited
                        visit.add((nr, nc))
                        q.append((nr, nc))
        
        #empty grid
        if not grid:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        visit = set()
        islands = 0
        
        for i in range(r):
            for j in range(c):
                
                #if land
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i, j)
                    islands += 1
                    
        return islands
        