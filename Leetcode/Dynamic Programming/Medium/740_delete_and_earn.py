# Runtime: 148 ms, faster than 7.65% of Python online submissions for Delete and Earn.
# Memory Usage: 12 MB, less than 28.57% of Python online submissions for Delete and Earn.

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        cnt = [0 for i in range(10001)]
        
        for i in nums:
            cnt[i] += 1
            
        using_prev = 0
        avoiding_prev = 0
        prev = -1
        
        for i in range(10001):
            
            mx = max(using_prev, avoiding_prev)
            
            if i-1 == prev: 
                # If want to use this, avoid the prev, so use value from avoid
                using_prev = avoiding_prev + i*cnt[i]
                avoiding_prev = mx
            else: 
                # Good to use, so add current value to value after using prev or avoiding prev which was better
                using_prev = i*cnt[i] + mx
                avoiding_prev = mx
            
            prev = i
        
        return max(using_prev, avoiding_prev)