# Runtime: 420 ms, faster than 34.08% of Python online submissions for Ugly Number II.
# Memory Usage: 12.8 MB, less than 67.27% of Python online submissions for Ugly Number II.

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        arr = [1]
        ptr = [0,0,0]
        mlt = [2,3,5]
        
        i = 0
        while i < n-1:
            
            resarr = [arr[ptr[j]] * mlt[j] for j in range(3)]
            res = min(resarr)
            ptr = [ptr[x] + (res == resarr[x]) for x in range(3)]
            arr.append(res)
            
            i += 1
        
        return arr[-1]