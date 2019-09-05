# Runtime: 16 ms, faster than 73.76% of Python online submissions for Pascal's Triangle.
# Memory Usage: 11.6 MB, less than 96.67% of Python online submissions for Pascal's Triangle.

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        numRows
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        ans = [[1], [1,1]]
        
        for i in range(2, numRows):
            arr = [1]
            for j in range(i-1):
                arr.append(ans[i-1][j] + ans[i-1][j+1])
            arr.append(1)
            ans.append(arr)
        
        return ans