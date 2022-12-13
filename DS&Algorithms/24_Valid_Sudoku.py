class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sud = {}
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if f"{i//3}, {j//3}, {board[i][j]}" in sud.keys() or rows[i].count(board[i][j]) or cols[j].count(board[i][j]):
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                sud[f"{i//3}, {j//3}, {board[i][j]}"] = 1
        return True
