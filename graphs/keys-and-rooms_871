class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        keys = []
        def visit(room):
            if rooms[room] == []:
                return

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    visit(key)
                
        visited.add(0)
        visit(0)
        if len(visited) == len(rooms):
            return True
        return False

        