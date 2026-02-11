class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter_total = 0
        for x in range(rows):
            for y in range(cols):
                perimeter = 0
                node = grid[x][y]
                if node:
                    perimeter = 4
                # borders
                    if x > 0 and grid[x-1][y] == 1:
                        perimeter-=2
                    if y > 0 and grid[x][y-1] == 1:
                        perimeter-=2
                perimeter_total+=perimeter
        return perimeter_total
        
