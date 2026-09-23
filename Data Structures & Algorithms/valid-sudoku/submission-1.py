from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_set = defaultdict(set)
        c_set = defaultdict(set)
        b_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': 
                    continue
                
                b = (r // 3) * 3 + (c // 3)
                if board[r][c] in r_set[r] or \
                   board[r][c] in c_set[c] or \
                   board[r][c] in b_set[b]:
                    return False
                
                r_set[r].add(board[r][c])
                c_set[c].add(board[r][c])
                b_set[b].add(board[r][c])

        return True

        