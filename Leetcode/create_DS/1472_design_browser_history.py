# Runtime: 244 ms, faster than 87.04% of Python online submissions for Design Browser History.
# Memory Usage: 15.6 MB, less than 100.00% of Python online submissions for Design Browser History.

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        
        self.arr = [homepage] + [None for _ in range(5000)]
        self.max = 0
        self.curr = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        
        self.curr += 1
        self.arr[self.curr] = url
        self.max = self.curr

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        
        ret = max(0, self.curr - steps)
        self.curr = ret
        return self.arr[self.curr]
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        
        ret = min(self.max, self.curr + steps)
        self.curr = ret
        return self.arr[self.curr]
    
    
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)