# Runtime: 60 ms, faster than 51.23% of Python online submissions for Min Stack.
# Memory Usage: 16.6 MB, less than 6.67% of Python online submissions for Min Stack.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.st = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.st.append(x)

        if self.min == None:
            self.min = x
        else:
            self.min = min(self.min, x)

    def pop(self):
        """
        :rtype: None
        """
        
        if len(self.st):
            self.st.pop()
            if len(self.st): 
                self.min = min(self.st)
            else:
                self.min = None
            
    def top(self):
        """
        :rtype: int
        """
        
        if len(self.st):
            return self.st[-1]
    
            
    def getMin(self):
        """
        :rtype: int
        """
        
        if self.min != None:
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()