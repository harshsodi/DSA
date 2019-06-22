# Runtime: 20 ms, faster than 96.29% of Python online submissions for Largest Number.
# Memory Usage: 11.9 MB, less than 21.06% of Python online submissions for Largest Number.

def comparator_function(x, y) :
    if y + x*pow(10, len(str(y))) < x + y*pow(10, len(str(x))):
        return 1
    return -1

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(cmp=comparator_function);
        while nums and nums[0] == 0:
            nums.remove(0)
            
        if nums == []:
            return "0"
        return "".join(map(str, nums))
        