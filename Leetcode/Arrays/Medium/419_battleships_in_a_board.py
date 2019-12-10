# Runtime: 52 ms, faster than 94.14% of Python online submissions for Battleships in a Board.
# Memory Usage: 14.9 MB, less than 58.33% of Python online submissions for Battleships in a Board.

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        m = len(board) # Num rows
        if m == 0:
            return 0
        n = len(board[0])
        
        total = 0
        
        for i in range(m):
            for j in range(n):
                
                if board[i][j] == 'X':
                    adj = 0
                    if i>0 and board[i-1][j] == 'X':
                        adj += 1
                    if i < m-1 and board[i+1][j] == 'X':
                        adj += 1
                    if j>0 and board[i][j-1] == 'X':
                        adj += 1
                    if j < n-1 and board[i][j+1] == 'X':
                        adj += 1
                    
                    if adj == 0:
                        total += 2
                    
                    if adj == 1:
                        total += 1
        
        return total / 2