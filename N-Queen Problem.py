class Solution:
    def nQueen(self, n):
        def is_safe(row, col):
            # Check if the column or the diagonals have a queen already
            return not (cols[col] or diag1[row - col] or diag2[row + col])
        
        def place_queen(row, col):
            # Place a queen on the board
            board[row] = col + 1
            cols[col] = True
            diag1[row - col] = True
            diag2[row + col] = True
        
        def remove_queen(row, col):
            # Remove a queen from the board
            board[row] = 0
            cols[col] = False
            diag1[row - col] = False
            diag2[row + col] = False
        
        def backtrack(row):
            if row == n:
                # Found a valid configuration, store it
                result.append(board[:])
                return
            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)
        
        # Initialize the board and the tracking arrays
        board = [0] * n
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)  # For the left diagonal
        diag2 = [False] * (2 * n - 1)  # For the right diagonal
        result = []
        
        backtrack(0)
        return result