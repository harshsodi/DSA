# Runtime: 3524 ms, faster than 5.60% of Python online submissions for Partition Array for Maximum Sum.
# Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Partition Array for Maximum Sum.

class Solution(object):

    def f(self, arr, K, i, group, actuali):
        
        if i == len(arr) - 1:
            return max(group) * len(group)
    
        alone = None
        if self.memo.get(actuali) != None:
            alone = self.memo[actuali]
        else:
            alone = self.f(arr[i+1:], K, 0, [arr[i+1]], actuali + 1) 
            self.memo[actuali] = alone
    
        aloneval = alone + (max(group) * len(group))
        if len(group) == K:
            return aloneval
        else:
            return max(aloneval, self.f(arr, K, i+1, group + [arr[i+1]], actuali + 1))
        
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        n = len(A)
        self.memo = {}
        
        return self.f(A, K, 0, [A[0]], 0)