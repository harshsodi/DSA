# Runtime: 40 ms, faster than 46.25% of Python online submissions for Delete Columns to Make Sorted II.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Delete Columns to Make Sorted II.

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        n = len(A)
        if n == 0:
            return 0
        slen = len(A[0])
        
        ans = 0
        l = ["" for _ in A]
        
        for i in range(slen):
            ltmp = [l[j] + A[j][i] for j in range(n)]
            
            issorted = True
            for x in range(1, n):
                if ltmp[x] < ltmp[x-1]:
                    issorted = False
                    break
        
            if issorted:
                l = ltmp
            else:
                ans += 1
        
        return ans