# Runtime: 556 ms, faster than 75.96% of Python online submissions for Split Array into Consecutive Subsequences.
# Memory Usage: 13 MB, less than 22.22% of Python online submissions for Split Array into Consecutive Subsequences.

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        
        f = {}
        
        for i in nums:
            if d[i] > 0:
                if f.get(i):
                    # Hume jaain kar lo
                    f[i] -= 1
                    f[i+1] = f.get(i+1,0) + 1
                else:
                    # Create own subsequence
                    if d.get(i+1) and d.get(i+2):
                        d[i+1] -= 1
                        d[i+2] -= 1
                        
                        f[i+3] = f.get(i+3, 0) + 1
                    else:
                        return False
                d[i] -= 1
        
        return True
            

        