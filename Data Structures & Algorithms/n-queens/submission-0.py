class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posidiag = set()
        negidiag = set()

        res = []
        board = [["."]* n for i in range (n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posidiag or (r - c) in negidiag:
                    continue

                col.add(c)
                posidiag.add(r + c)
                negidiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posidiag.remove(r + c)
                negidiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res