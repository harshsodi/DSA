# Runtime: 160 ms, faster than 90.58% of Python online submissions for Minesweeper.
# Memory Usage: 12.5 MB, less than 42.86% of Python online submissions for Minesweeper.

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        m = len(board)
        n = len(board[0])
        
        ci = click[0]
        cj = click[1]
        
        if board[ci][cj] == 'M':
            board[ci][cj] = 'X'
            return board
        
        adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        q = [[ci, cj]]
        v = {(ci, cj): True}
        
        while len(q):    
            top = q.pop(0)                
        
            nmines = 0
            next_level = []
            for i in adj:
                nxti = top[0] + i[0]
                nxtj = top[1] + i[1]
                
                if 0<=nxti<m and 0<=nxtj<n:
                    
                    if board[nxti][nxtj] == 'M':
                        nmines += 1
            
                    if board[nxti][nxtj] == 'E':
                        if v.get((nxti, nxtj)) == None:
                            next_level += [[nxti, nxtj]]
                        
                            
            if nmines == 0:
                q = q + next_level
                for nxt in next_level:
                    v[tuple(nxt)] = True
                board[top[0]][top[1]] = 'B'
            else:
                board[top[0]][top[1]] = str(nmines)
        
        return board