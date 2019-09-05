# Runtime: 28 ms, faster than 90.18% of Python online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 14.8 MB, less than 38.46% of Python online submissions for Minimum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution(object):
    
    def f(self, root, d):
        
        if root.left == None and root.right == None:
            self.ans = min(self.ans, d)
    
        if root.left != None: 
            self.f(root.left, d+1)
            
        if root.right != None:
            self.f(root.right, d+1)
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        self.ans = sys.maxsize 
        self.f(root, 1)
        
        return self.ans