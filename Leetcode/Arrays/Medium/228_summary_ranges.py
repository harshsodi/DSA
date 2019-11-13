# Runtime: 12 ms, faster than 89.28% of Python online submissions for Summary Ranges.
# Memory Usage: 11.8 MB, less than 47.06% of Python online submissions for Summary Ranges.

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        n = len(nums)
        
        if n == 0:
            return []
        
        ans = []
        p = 0
        i = 1
        while i < n:
            if nums[i] != nums[i-1] + 1:
                print nums[p], nums[i-1]
                
                if p == i-1:
                    ans.append(str(nums[p]))
                else:
                    ans.append(str(nums[p]) + "->" + str(nums[i-1]))
                
                p = i
            i += 1
        
        if p == i-1:
            ans.append(str(nums[p]))
        else:
            ans.append(str(nums[p]) + "->" + str(nums[i-1]))
        
        return ans