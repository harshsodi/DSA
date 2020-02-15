# Runtime: 36 ms, faster than 81.25% of Python online submissions for Filling Bookcase Shelves.
# Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Filling Bookcase Shelves.

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        
        n = len(books)
        mem = {}
        
        def f(i, rw, h):
            
            if i == n:
                return h
            
            a = float('inf')
            b = float('inf')
            
            if rw >= books[i][0]:
                a = f(i+1, rw - books[i][0], max(h, books[i][1]))

            if mem.get((i+1, shelf_width - books[i][0])):
                b = h + mem[(i+1, shelf_width - books[i][0])]
            else:
                x = f(i+1, shelf_width - books[i][0], books[i][1])
                mem[(i+1, shelf_width - books[i][0])] = x
                b = h + x
            
            return min(a,b)    
            
        return f(1, shelf_width - books[0][0], books[0][1])