# Runtime: 48 ms, faster than 69.19% of Python online submissions for Rotate Array.
# Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Rotate Array.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n <= 1 or k == 0 or n == k:
            return
        
        s = 0
        j = 0
        t = nums[j]
        
        for i in range(n):
            
            r = (j+k)%n
            x = nums[r]
            nums[r] = t
            t = x
            j = r
            
            if r == s:
                j = (r+1)%k
                t = nums[j]
                s = j