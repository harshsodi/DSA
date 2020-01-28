# Runtime: 896 ms, faster than 31.21% of Python online submissions for Partition to K Equal Sum Subsets.
# Memory Usage: 11.8 MB, less than 60.00% of Python online submissions for Partition to K Equal Sum Subsets.

class Solution(object):
    
    def f(self, nums, i, d, k, r):
        
        # print d
        
        if i == len(nums):
            for x in d:
                if x != r:
                    return False
            return True
        
        fin = False
        
        for j in range(k):
            
            if j > 0 and (d[j-1] == None):
                break
            
            do = d[j]
            
            if d[j] == None:
                d[j] = nums[i]   
            else:
                if d[j] + nums[i] > r:
                    continue
                
                d[j] += nums[i]
            
            if self.f(nums, i+1, d, k, r):
                d[j] = do
                return True
        
            d[j] = do

        return False
        
        
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        nums.sort(reverse = True)
        s = sum(nums)
        r = None
        
        if s % k != 0:
            return False
    
        r = s/k
    
        if nums[-1] > r:
            return False
        
        print s, k, r
        d = [None for _ in range(k)]
        d[0] = nums[0]
        
        return self.f(nums, 1, d, k, r)