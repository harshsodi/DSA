# Runtime: 28 ms, faster than 61.95% of Python online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12 MB, less than 36.74% of Python online submissions for Search in Rotated Sorted Array.

def f(x, m, l):
    return (x+m)%l

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        l = 0
        r = n-1

        while l<=r:
            m = (l+r)/2
            if nums[m] <= nums[n-1]:
                r = m - 1
            else:
                l = m + 1

        print l
        x = l
        
        l2 = 0
        r2 = n-1
        
        while l2<=r2:
            m = (l2+r2)/2
            pos = (x+m)%n
            if nums[pos] == target:
                return pos
            if nums[pos] < target:
                l2 = m + 1
            else:
                r2 = m - 1
        
        return -1
                