# Runtime: 84 ms, faster than 48.35% of Python online submissions for Combination Sum.
# Memory Usage: 11.7 MB, less than 79.59% of Python online submissions for Combination Sum.

class Solution(object):

    def f(self, s, l, t, arr, i):
        
        if s == t:
            self.ans.append(l)
            return
        if s > t:
            return
        
        for i in range(i, len(arr)):
            self.f(s+arr[i], l+[arr[i]], t, arr, i)
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        self.ans = []
        self.f(0, [], target, candidates, 0)
        
        return self.ans