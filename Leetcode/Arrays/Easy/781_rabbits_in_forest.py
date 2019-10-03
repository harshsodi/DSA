# Runtime: 28 ms, faster than 81.33% of Python online submissions for Rabbits in Forest.
# Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Rabbits in Forest.

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        
        d = {}
        
        total = 0
        for i in answers:
            if i == 0:
                total += 1
                continue
            d[i] = d.get(i, 0) + 1
        
        for k in d:
            v = d[k]
            x = (v/(k+1))*(k+1)
            total += x
            if x != v:
                total += (k+1)
        
        return total