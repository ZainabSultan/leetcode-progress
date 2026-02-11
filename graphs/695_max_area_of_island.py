class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        def max_area(x,y):
            if not ( 0 <= x < rows and 0 <= y < cols) or grid[x][y] == 0:
                return 0 


            grid[x][y] = 0

            area = 1
            area += max_area(x+1, y)
            area += max_area(x-1, y)
            area += max_area(x, y+1)
            area += max_area(x, y-1)

            return area
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    area = max_area(x,y)
                    res = max(res, area)

        return res

        
