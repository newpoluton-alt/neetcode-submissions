class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i]
            column = [board[n][i] for n in range(len(board))]
            grid = [board[r + (int(i / 3) * 3)][c + (i - int(i/ 3)* 3) * 3] for r in range(3) for c in range(3)]

            for j in range(len(row)):

                tempRow = list(filter(lambda x: x!= ".", row[:]))
                tempColumn = list(filter(lambda x: x != ".", column[:]))
                tempGrid = list(filter(lambda x: x != ".", grid[:]))


                if j + 1 <= len(tempRow):
                    re = tempRow.pop(j)
                    if re in tempRow:
                        return False

                if j + 1 <= len(tempColumn):
                    ce = tempColumn.pop(j)        
                    if ce in tempColumn:
                        return False
                
                if j + 1 <= len(tempGrid):
                    ge = tempGrid.pop(j)
                    if ge in tempGrid:
                        return False
            
        else:
            return True
