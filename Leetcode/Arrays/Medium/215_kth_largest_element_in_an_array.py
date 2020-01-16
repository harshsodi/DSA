# Runtime: 900 ms, faster than 17.98% of Python online submissions for Kth Largest Element in an Array.
# Memory Usage: 12.3 MB, less than 62.26% of Python online submissions for Kth Largest Element in an Array.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def partition(arr, l, r):
            
            p = r
    
            i = l
            j = r
            
            while i < j:
                while i < j and arr[i] >= arr[p]:
                    i += 1
                while i < j and arr[j] <= arr[p]:
                    j -= 1
                
                arr[i], arr[j] = arr[j], arr[i]
            
            if arr[i] < arr[p]:
                arr[i], arr[p] = arr[p], arr[i]
            
            return i
            
        n = len(nums)    
            
        l = 0
        r = n - 1
        
        while True:
            pos = partition(nums, l, r)
        
            # print nums, pos, k-1
        
            if pos > k-1:
                r = pos - 1
            elif pos < k-1:
                l = pos + 1
            else:
                return nums[pos]