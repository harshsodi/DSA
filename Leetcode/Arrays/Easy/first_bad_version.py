# Runtime: 8 ms, faster than 98.70% of Python online submissions for First Bad Version.
# Memory Usage: 11.8 MB, less than 32.46% of Python online submissions for First Bad Version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lo = 1
        hi = n
        
        f = -1
        
        while lo <= hi:
            
            mid = (lo + hi)/2
            print mid, isBadVersion(mid)
            
            if isBadVersion(mid):
                f = mid
                hi = mid - 1
                
                if mid > 1 and not isBadVersion(mid-1):
                    break
            else:
                lo = mid + 1
        
        if f != -1:
            return f
        else:
            return -1