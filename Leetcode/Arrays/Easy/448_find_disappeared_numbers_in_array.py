# Runtime: 364 ms, faster than 20.18% of Python online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 19.1 MB, less than 50.00% of Python online submissions for Find All Numbers Disappeared in an

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        ans = []
        
        for i in range(n):
            x = abs(nums[i]) - 1
            nums[x] = abs(nums[x])*-1
        
        for i in range(n):
            if nums[i]>0:
                ans.append(i+1)
                
        return ans