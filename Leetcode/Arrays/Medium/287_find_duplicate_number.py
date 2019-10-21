# Runtime: 56 ms, faster than 44.80% of Python online submissions for Find the Duplicate Number.
# Memory Usage: 13.6 MB, less than 50.00% of Python online submissions for Find the Duplicate Number.

class Solution(object):
    def findDuplicate(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        t = a[0]
        h = a[0]

        print t, h

        while True:

            t = a[t]
            h = a[a[h]]

            print t, h

            if t == h:
                break

        p1 = a[0]
        p2 = t
        while p1 != p2:
            p1 = a[p1]
            p2 = a[p2]

        return p1