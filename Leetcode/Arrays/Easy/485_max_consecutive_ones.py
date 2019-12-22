# Runtime: 332 ms, faster than 60.58% of Python online submissions for Max Consecutive Ones.
# Memory Usage: 11.9 MB, less than 68.42% of Python online submissions for Max Consecutive Ones.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 0:
            return 0
        
        l = 0
        r = 0
        
        max_ans = 0
        temp_ans = 0
        
        while l < n:
            while l<n and nums[l] == 0:
                l += 1
            
            while l < n and nums[l] == 1:
                temp_ans += 1
                l += 1
            
            max_ans = max(max_ans, temp_ans)
            
            temp_ans = 0
        
        return max_ans