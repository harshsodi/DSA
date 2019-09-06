# Runtime: 40 ms, faster than 97.84% of Python online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 11.8 MB, less than 98.18% of Python online submissions for Two Sum II - Input array is sorted.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        length = len(numbers)
        
        l = 0
        r = length - 1
        
        while True:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]