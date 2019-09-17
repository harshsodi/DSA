# Runtime: 132 ms, faster than 27.46% of Python online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.7 MB, less than 11.11% of Python online submissions for K-diff Pairs in an Array.

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k<0:
            return 0
        
        l = len(nums)
        d = {}
        dedup = {}
        
        for i in range(l):
            if d.get(nums[i]) == None:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        
        for i in range(l):
            comp_l = nums[i] - k
            comp_r = nums[i] + k
            
            if d.get(comp_l) != None:
                for ind in d[comp_l]:
                    if ind != i:
                        s = (comp_l, nums[i])
                        if not dedup.get(s):
                            dedup[s] = True
                            
            if d.get(comp_r) != None:
                for ind in d[comp_r]:
                    if ind != i:
                        s = (nums[i], comp_r)
                        if not dedup.get(s):
                            dedup[s] = True
        
        return len(dedup.keys())