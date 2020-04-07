# Runtime: 820 ms, faster than 88.65% of Python online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 13.5 MB, less than 50.00% of Python online submissions for Max Sum of Rectangle No Larger Than K.

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        import bisect
        
        ans = float('-inf')
        
        for l in range(n):
            # print "---"
            sm = [0 for _ in range(m)]
            for r in range(l, n):
                for row in range(m):
                    sm[row] += matrix[row][r]
                
                srt = [0]
                prsum = 0
                for pr in sm:
                    prsum += pr
                    pos = bisect.bisect_left(srt, prsum - k)
                    if pos < len(srt):
                        ans = max(ans, prsum - srt[pos])
                    bisect.insort(srt, prsum)
                    
        return ans