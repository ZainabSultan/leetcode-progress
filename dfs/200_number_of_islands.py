class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def island(x, y):
            if not (0<= x < rows and 0 <= y < cols) or grid[x][y] == '0':
                return
            
            grid[x][y] = '0' # mark visited

            island(x+1,y)
            island(x-1,y)
            island(x,y+1)
            island(x,y-1)

        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    island(x,y)
                    res+=1
                    
        return res

             
            