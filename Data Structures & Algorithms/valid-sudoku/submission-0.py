class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        valid = {}
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == ".":
                    continue
                value = board[row][column]
                div=0
                if row<= 2 and column <= 2:
                    div = 0
                elif row<= 2 and column>2 and column<=5:
                    div = 1
                elif row<= 2 and column>5 and column<=8:
                    div = 2
                elif row>2 and row<=5 and column<=2:
                    div = 3
                elif row>2 and row<=5 and column>2 and column<=5:
                    div = 4
                elif row>2 and row<=5 and column>5 and column<=8:
                    div = 5
                elif row>5 and row<=8 and column<=2:
                    div = 6
                elif row>5 and row<=8 and column>2 and column<=5:
                    div = 7
                elif row>5 and row<=8 and column>5 and column<=8:
                    div = 8
                # 1. If we haven't seen this number yet, create its dictionary and empty sets
                if value not in valid:
                    valid[value] = {"rows": set(), "columns": set(), "div": set()}

                # 2. Check if the current row, column, or div already exists in this number's sets
                if (row in valid[value]["rows"] or 
                    column in valid[value]["columns"] or 
                    div in valid[value]["div"]):
                    return False # We found a duplicate!

                # 3. If it's not a duplicate, add the current indices to the sets so we remember them
                valid[value]["rows"].add(row)
                valid[value]["columns"].add(column)
                valid[value]["div"].add(div)
        return True