# Runtime: 88 ms, faster than 81.40% of Python online submissions for Champagne Tower.
# Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Champagne Tower.

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
        row = 0
        curr_row = [poured]
        
        while True:
            
            next_row = [0 for _ in range(row+2)]
            
            for i_ in range(len(curr_row)):
                i = curr_row[i_]
                
                if row == query_row and i_ == query_glass:
                    return min(1, i)
                
                rem = i-1
                
                if rem > 0:
                    overflow = rem/2.0
                    next_row[i_] += overflow
                    next_row[i_+1] += overflow
            
            curr_row = next_row
            row += 1