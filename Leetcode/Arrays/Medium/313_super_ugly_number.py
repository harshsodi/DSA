# Runtime: 980 ms, faster than 61.35% of Python online submissions for Super Ugly Number.
# Memory Usage: 15.5 MB, less than 97.92% of Python online submissions for Super Ugly Number.

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        m = len(primes)
        arr = [1]
        ptr = [0 for _ in range(m)]
        mlt = primes
        
        i = 0
        while i < n-1:
            
            resarr = [arr[ptr[j]] * mlt[j] for j in range(m)]
            res = min(resarr)
            ptr = [ptr[x] + (res == resarr[x]) for x in range(m)]
            arr.append(res)
            
            i += 1
        
        return arr[-1]