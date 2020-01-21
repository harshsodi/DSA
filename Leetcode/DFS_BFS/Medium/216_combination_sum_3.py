# Runtime: 16 ms, faster than 85.56% of Python online submissions for Combination Sum III.
# Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Combination Sum III.

class Solution(object):
    
    def dfs(self, arr, s, n, k, level):
        
        # print arr
        
        if level > k:
            return
        
        last = arr[-1]
        
        for i in range(last+1, 10):
            if i + s == n and level == k-1:
                self.ans.append(arr[1:] + [i])
            else:
                self.dfs(arr + [i], s+i, n, k, level+1)
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        self.ans = []
        self.dfs([0], 0, n, k, 0)
        
        return self.ans