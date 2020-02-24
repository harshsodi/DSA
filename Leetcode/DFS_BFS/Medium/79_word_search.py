# Runtime: 496 ms, faster than 11.09% of Python online submissions for Word Search.
# Memory Usage: 18.2 MB, less than 6.67% of Python online submissions for Word Search.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        
        l = len(word)
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def f(i, j, path):
            
            if (i, j) in path:
                return False
                         
            if len(path) == l:
                return True
            
            if i < 0 or i >=m or j < 0 or j >=n:
                return False
            
            if board[i][j] != word[len(path)]:
                return False
            
            ans = f(i+1, j, path+[(i, j)]) or f(i, j+1, path+[(i, j)]) or f(i-1, j, path+[(i, j)]) or f(i, j-1, path+[(i, j)])
        
            return ans    
        
        for i in range(m):
            for j in range(n):
                if f(i, j, []):
                    return True
        
        return False