# Runtime: 268 ms, faster than 9.87% of Python online submissions for Surrounded Regions.
# Memory Usage: 30.3 MB, less than 14.29% of Python online submissions for Surrounded Regions.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        
        v = {}
        adjs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                
                if v.get((i,j)) != None or board[i][j] == 'X':
                    continue
                
                clan = [[i, j]]
                q = [[i, j]]
                v[(i,j)] = True
                lv = {}  
            
                while len(q):
                    top = q.pop(0)
                    
                    for mv in adjs:
                        nxti = top[0] + mv[0]
                        nxtj = top[1] + mv[1]
                        
                        
                        if 0<nxti<(m-1) and 0<nxtj<(n-1):
                            if board[nxti][nxtj] == 'O' and lv.get((nxti, nxtj)) == None:
                                q.append([nxti, nxtj])
                                clan.append([nxti, nxtj])        
                                lv[(nxti, nxtj)] = True
                                v[(nxti, nxtj)] = True
                        else:
                            if board[nxti][nxtj] == 'O':
                                clan = []
                                q = []
                                break
                
                # print clan
                for c in clan:
                    board[c[0]][c[1]] = 'X'