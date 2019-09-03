# Runtime: 28 ms, faster than 78.92% of Python online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 14.6 MB, less than 48.15% of Python online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution(object):

    def f(self,T, d):
        if T == None:
            self.max_d = max(self.max_d, d)
            return
        
        self.f(T.left, d+1)
        self.f(T.right, d+1)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        self.max_d = 0        
        self.f(root, 0)
        
        return self.max_d
        
        