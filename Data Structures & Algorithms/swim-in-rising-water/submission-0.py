class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) # We are having a square grid
        visit = set()
        minheap = [[grid[0][0], 0, 0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visit.add((0,0))

        while minheap:
            t,r,c = heapq.heappop(minheap)

            if r == N-1 and c == N-1:
                return t
            for dr,dc in directions:
                neighR, neighC = r + dr, c + dc
                if (neighR == N or neighC == N or neighR < 0 or 
                    neighC < 0 or (neighR,neighC) in visit):
                    continue
                visit.add((neighR,neighC))
                heapq.heappush(minheap,[max(t,grid[neighR][neighC]),neighR,neighC])