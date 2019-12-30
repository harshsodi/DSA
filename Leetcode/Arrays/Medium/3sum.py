# Runtime: 964 ms, faster than 32.86% of Python online submissions for 3Sum.
# Memory Usage: 15.2 MB, less than 21.15% of Python online submissions for 3Sum.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0)+1
            
        
        arr = sorted([k for k, v in d.items()])
        n = len(arr)
        
        ans = {}
        
        for i in range(n):
            hinge = arr[i]
            
            for j in range(i, n):
                mid = arr[j]
                
                if hinge == mid and d[hinge] < 2:
                    continue
                
                target = -hinge-mid
                
                if d.get(target) != None:
                    c = d[target]
                    
                    if mid == target:
                        c -= 1
                    
                    if hinge == target:
                        c -= 1
                    
                    if c > 0:
                        ans[tuple(sorted([hinge, mid, target]))] = True
            
        return ans.keys()