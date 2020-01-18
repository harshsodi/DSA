# Runtime: 640 ms, faster than 93.88% of Python online submissions for Fruit Into Baskets.
# Memory Usage: 17.2 MB, less than 20.00% of Python online submissions for Fruit Into Baskets.

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        n = len(tree)
        if n<3:
            return n
        
        maxlen = 0
                
        d = {}
        d[tree[0]] = 0
        
        t1 = tree[0]
        t2 = -1
        
        i = 0
        j = 1
        
        while j < n:
            if tree[j] != tree[j-1]:
                d[tree[j]] = j    
                
                if tree[j] != t1 and tree[j] != t2:
                    t1 = tree[j-1]
                    t2 = tree[j]
                    
                    maxlen = max(maxlen, j - i)
                    i = d[tree[j-1]]
        
            j += 1
        
        maxlen = max(maxlen, j-i)
        
        return maxlen
    