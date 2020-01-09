# Runtime: 232 ms, faster than 74.42% of Python online submissions for Maximum Subarray Sum with One Deletion.
# Memory Usage: 19.6 MB, less than 100.00% of Python online submissions for Maximum Subarray Sum with One Deletion.

class Solution(object):
    
    def maximumSum(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        ans = nums[0]
        d = 0
        nd = nums[0]
        
        for i in range(1, n):
            d = max(d+nums[i], nd)
            nd = max(nd+nums[i], nums[i])
            ans = max([ans, d, nd])
        
        return ans