# Runtime: 192 ms, faster than 82.85% of Python online submissions for Continuous Subarray Sum.
# Memory Usage: 12.9 MB, less than 25.00% of Python online submissions for Continuous

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        n = len(nums)
        
        k = abs(k)
        
        if k == 1:
            return n >= 2
        
        if k == 0:
            cnt = 0
            for i in nums:
                if i == 0:
                    cnt += 1
                else:
                    cnt = 0
                
                if cnt >= 2:
                    return True
            
            return False
        
        sm = 0
        mem = {0: -1}
        
        for i in range(n):
            sm += nums[i]
        
            if sm%k == 0 and i >= 2:
                return True
            
            req = sm%k
            
            chk = mem.get(req)
            if chk != None and (i - chk) >= 2:
                return True
        
            mem[req] = min(mem.get(req, float('inf')), i)
        
        return False