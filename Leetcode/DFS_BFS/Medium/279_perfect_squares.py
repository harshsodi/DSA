# Runtime: 64 ms, faster than 97.95% of Python online submissions for Perfect Squares.
# Memory Usage: 12.4 MB, less than 28.00% of Python online submissions for Perfect Squares.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def is_square(integer):
            # print integer
            root = math.sqrt(integer)
            return integer == int(root + 0.5) ** 2
        
        i = 1
        squares = []
        
        while True:
            s = i*i
            if s < n:
                squares.append(s)
                i += 1
            else:
                break
        
        squares = list(reversed(squares))
        
        q = [[n]]
        while q:
            curr = q.pop(0)
            last = curr[-1]
            
            if is_square(last):
                return len(curr)
        
            for sq in squares:
                sq_comp = last - sq
                if sq_comp > 0:
                    if is_square(sq_comp):
                        return len(curr) + 1
                    q.append(curr[:-1] + [sq, sq_comp])