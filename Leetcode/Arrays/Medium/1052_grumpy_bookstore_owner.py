# Runtime: 268 ms, faster than 54.49% of Python online submissions for Grumpy Bookstore Owner.
# Memory Usage: 13.7 MB, less than 100.00% of Python online submissions for Grumpy Bookstore Owner.

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        
        n = len(grumpy)
        
        arr = []
        for i in range(n):
            if grumpy[i] == 1:
                arr.append(customers[i])
            else:
                arr.append(0)
        
        # print arr
        
        l = 0
        r = 0
        
        arrsum = arr[l]
        msum = arrsum
        
        while r < n-1 and r < X-1:
            r += 1
            arrsum += arr[r]
            msum = max(msum, arrsum)
        
        while r < n-1:
            r += 1
            arrsum += arr[r]
            arrsum -= arr[l]
            l += 1
            
            msum = max(arrsum, msum)
        
        # print arr
        # print msum
        
        actualsum = 0
        for i in range(n):
            if grumpy[i] == 0:
                actualsum += customers[i]
        
        return actualsum + msum