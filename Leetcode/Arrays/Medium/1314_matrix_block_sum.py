# Runtime: 316 ms, faster than 100.00% of Python online submissions for Matrix Block Sum.
# Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Matrix Block Sum.

class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        
        mat_pre = [[0 for _ in range(n)] for x in range(m)]
        mat_ans = [[0 for _ in range(n)] for x in range(m)]
        
        for i in range(m):
            s = 0
            for j in range(n):
                s += mat[i][j]
                mat_pre[i][j] = s
        
        for i in range(m):
            for j in range(n):
                top = max(0, i-K)
                bottom = min(m-1, i+K)
                left = max(0, j-K)
                right = min(n-1, j+K)
                
                ans = 0
                
                for x in range(top, bottom+1):
                    ans += mat_pre[x][right] - mat_pre[x][left] + mat[x][left]
                
                mat_ans[i][j] = ans
        
        return mat_ans