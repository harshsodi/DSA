# Runtime: 28 ms, faster than 97.09% of Python online submissions for Move Zeroes.
# Memory Usage: 12.9 MB, less than 13.93% of Python online submissions for Move Zeroes.

class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = len(arr)
        current_index = 0
        
        for i in range(l):
            if arr[i] != 0:
                arr[current_index] = arr[i]
                current_index += 1
        
        for i in range(current_index, l):
            arr[i] = 0