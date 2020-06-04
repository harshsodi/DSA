# Runtime: 64 ms, faster than 74.68% of Python online submissions for Recover Binary Search Tree.
# Memory Usage: 13.2 MB, less than 14.29% of Python online submissions for Recover Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))
        
        def f(root):
            
            if root == None:
                return
            
            f(root.left)
            
            # Do stuff with this element
            if root.val < self.prev.val:
                if self.first == None:
                    self.first = self.prev
                if self.first != None:
                    self.second = root
            
            self.prev = root
            
            f(root.right)
        
        f(root)
        self.first.val, self.second.val = self.second.val, self.first.val