# Runtime: 16 ms, faster than 99.21% of Python online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 17.6 MB, less than 75.00% of Python online submissions for Maximum Difference Between Node and Ancestor.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, maxval, minval):
                
        if root == None:
            return
    
        # print root.val, maxval, minval
    
        maxdiff = abs(root.val - maxval)
        mindiff = abs(root.val - minval)
    
        self.ans = max(self.ans, max(maxdiff, mindiff))
        
        maxval = max(maxval, root.val)
        minval = min(minval, root.val)
        
        self.f(root.left, maxval, minval)
        self.f(root.right, maxval, minval)
    
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = -float('inf')
        self.f(root.left, root.val, root.val)
        self.f(root.right, root.val, root.val)
        
        return self.ans