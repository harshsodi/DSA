# Runtime: 72 ms, faster than 80.10% of Python online submissions for Robot Return to Origin.
# Memory Usage: 12 MB, less than 81.82% of Python online submissions for Robot Return to Origin.

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        d = {'L':0, 'R':0, 'U':0, 'D':0}
        
        for i in moves:
            d[i] += 1
        
        if d['L'] == d['R'] and d['U'] == d['D']:
            return True
        return False