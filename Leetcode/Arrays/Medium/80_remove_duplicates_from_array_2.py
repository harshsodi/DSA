# Runtime: 36 ms, faster than 91.03% of Python online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 11.7 MB, less than 65.00% of Python online submissions for Remove Duplicates from Sorted Array II.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 0:
            return 0
        
        sh = 0
        
        curr = nums[0]
        cnt = 1
        for i in range(1, n):
            if nums[i] == curr:
                cnt += 1
                if cnt > 2:
                    sh += 1
                else:
                    nums[i-sh] = nums[i]
            else:
                nums[i-sh] = nums[i]
                curr = nums[i]
                cnt = 1
        
        return n-sh