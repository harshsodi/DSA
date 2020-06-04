# Runtime: 48 ms, faster than 54.38% of Python online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 15.8 MB, less than 100.00% of Python online submissions for N-ary Tree Postorder Traversal.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        self.ans = []
        
        def f(root):
            
            if root == None:
                return
        
            for i in root.children:
                f(i)
            
            self.ans.append(root.val)
        
        f(root)
        return self.ans