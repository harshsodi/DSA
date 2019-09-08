# Runtime: 12 ms, faster than 92.97% of Python online submissions for Invert Binary Tree.
# Memory Usage: 12 MB, less than 7.50% of Python online submissions for Invert Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root):
        
        if root == None:
            return root
    
        left = self.f(root.left)
        right = self.f(root.right)
        
        root.left = right
        root.right = left
        
        return root
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        return self.f(root)