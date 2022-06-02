class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            rows = [int(x) for x in board[i] if x.isdigit()]
            #extract each row
            
            tmpcol = [x[i] for x in board]
            cols = [int(x) for x in tmpcol if x.isdigit()]
            #extract each column
            
            for n in rows:
                if rows.count(n) != 1:
                    return False
                    
            for n in cols:
                if cols.count(n) != 1:
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmpgrid = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j+3]
                grid = [int(x) for x in tmpgrid if x.isdigit()]
                #extract each 3 by 3 grid
                
                for n in grid:
                    if grid.count(n) != 1:
                        return False
        
        return True
        