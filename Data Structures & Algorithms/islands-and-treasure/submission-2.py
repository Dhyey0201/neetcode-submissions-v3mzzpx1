class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()

        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        def addroom(r,c):
            if (r< 0 or r == ROWS or c<0 or c==COLS or (r,c) in visit or grid[r][c]==-1):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # 0 Means we found room
                    visit.add((r,c))
                    q.append([r,c])
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=distance
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            distance+=1
