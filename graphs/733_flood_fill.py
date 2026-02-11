class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        def flood(x,y, original_color=original_color):
            
            if x > len(image) - 1 or x < 0 or y > len(image[0]) - 1 or y < 0 or image[x][y] != original_color:
                return
            
            if image[x][y] == color:
                return 

            if image[x][y] == original_color:  
                image[x][y] = color
            
            flood(x+1, y)
            flood(x-1, y)
            flood(x, y+1)
            flood(x, y-1)
        
        
        flood(sr, sc)
        return image
