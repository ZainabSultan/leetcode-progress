class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == []:
            return -1 if n > 1 else 1
        degrees = defaultdict(int)

        for edge in trust:
            degrees[edge[1]]+=1
            degrees[edge[0]]-=1
        
        if max(degrees.values()) == n-1:
            return max(degrees, key = degrees.get)
        return -1
        
