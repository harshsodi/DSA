# Runtime: 276 ms, faster than 18.37% of Python online submissions for Combination Sum II.
# Memory Usage: 11.9 MB, less than 32.26% of Python online submissions for Combination Sum II.

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        n = len(candidates)
        
        mem = {}
        ans = []
        
        def f(path, last, curr_sum):
            
            if curr_sum == target and mem.get(tuple(sorted(path))) == None:
                ans.append(path)
                mem[tuple(sorted(path))] = True
            
            if curr_sum > target:
                return
            
            for i in range(last+1, n):
                f(path+[candidates[i]], i, curr_sum+candidates[i])    
        
        f([], -1, 0)
        
        return ans