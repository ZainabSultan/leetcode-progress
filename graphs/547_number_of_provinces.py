class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
                       
        n = len(isConnected)
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbour in range(n):
                nei = isConnected[city][neighbour]
                if nei == 1 and neighbour not in visited:
                    dfs(neighbour)
        
        prov = 0
        for i in range(n):
            if i not in visited:
                prov+=1
                dfs(i)
        return prov

                    


        