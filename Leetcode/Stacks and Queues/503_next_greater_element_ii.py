# Runtime: 204 ms, faster than 73.27% of Python online submissions for Next Greater Element II.
# Memory Usage: 13.8 MB, less than 25.00% of Python online submissions for Next Greater Element II.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        
        ans = [-1]*n
        
        s = []

        for i in range(n):
            if len(s) > 0:
                while len(s) and s[-1][1] < nums[i]:
                    ans[s.pop()[0]] = nums[i]
                
            s.append((i, nums[i]))
        
        for i in range(n):
            while len(s) and s[-1][1] < nums[i]:
                ans[s.pop()[0]] = nums[i]
        
        return ans