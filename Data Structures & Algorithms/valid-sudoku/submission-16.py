class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # key == row number, value == cell content
        row_content = defaultdict(list[str])
        # key == column number, value == cell content
        column_content = defaultdict(list[str])
        # sub_box_content[x] stores the numbers in box x
        sub_box_content = [[] for _ in range(9)]

        only_digits = [[] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                cell_content = board[i][j]
                box_number = (i // 3) * 3 + (j // 3)
                if cell_content != ".":
                    row_content[i].append(cell_content)
                    column_content[j].append(cell_content)
                    sub_box_content[box_number].append(cell_content)

        for i in range(9):
            # check if a row has duplicate digits
            if len(row_content[i]) != len(set(row_content[i])):
                return False
            # check if a column has duplicate digits
            if len(column_content[i]) != len(set(column_content[i])):
                return False
            # check if a sub-box has duplicate digits
            if len(sub_box_content[i]) != len(set(sub_box_content[i])):
                return False
        
        return True