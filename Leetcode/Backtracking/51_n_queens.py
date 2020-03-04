# Runtime: 68 ms, faster than 66.34% of Python online submissions for N-Queens.
# Memory Usage: 12.6 MB, less than 8.33% of Python online submissions for N-Queens.

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        rowd = {}
        cold = {}
        
        diag_1 = {}
        diag_2 = {}
        
        def is_safe(i,j):
            if rowd.get(i, False) != False  or cold.get(j, False) != False:
                return False
            
            if diag_1.get(i-j, False) != False or diag_2.get(i+j, False) != False:
                return False
        
            return True
                
        def f(board, i):
            
            # print board
            
            if i == n:
                ans.append([[x for x in y] for y in board])
                return
            
            for j in range(n):

                if not is_safe(i, j):
                    continue

                board[i][j] = 'Q'
                rowd[i] = True
                cold[j] = True
                diag_1[i-j] = True
                diag_2[j+i] = True

                f(board, i+1)

                board[i][j] = '.'
                rowd[i] = False
                cold[j] = False
                diag_1[i-j] = False
                diag_2[j+i] = False
            
        ans = []
        iboard = [["." for h in range(n)] for _ in range(n)]
        f(iboard, 0)
        
        for i in range(len(ans)):
            for j in range(n):
                ans[i][j] = "".join(ans[i][j])

        return ans