class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        col = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        for i in range( len(board)):
            for j in range(len(board)):

                if board[i][j] == ".":
                    continue

                box_id = (i // 3) * 3 + (j//3)
                val = board[i][j]
                if val in rows[i] or val in col[j] or val in  boxes[box_id]:
                    return False
                rows[i].add(val)
                col[j].add(val)
                boxes[box_id].add(val)
        
        return True
        


