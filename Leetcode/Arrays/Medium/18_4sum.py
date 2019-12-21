# Runtime: 168 ms, faster than 68.21% of Python online submissions for 4Sum.
# Memory Usage: 16.1 MB, less than 13.64% of Python online submissions for 4Sum.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        
        d = {}
        
        for i in range(n):
            for j in range(i+1, n):
                if i == j:
                    continue
                
                sm = nums[i] + nums[j]
                if d.get(sm) == None:
                    d[sm] = [(i, j)]
                else:
                    d[sm].append((i, j))
        
        ans = {}
        
        for p in d:
            x = d[p]
            # print p, x
            comp = target - p
            y = d.get(comp, [])
            
            for i in x:
                for j in y:
                    e1 = i[0]
                    e2 = i[1]
                    e3 = j[0]
                    e4 = j[1]
                    
                    l = [e1,e2,e3,e4]
                    
                    if len(set(l)) == 4:
                        ans[tuple(sorted([nums[x] for x in l]))] = True
                        
        return ans.keys()