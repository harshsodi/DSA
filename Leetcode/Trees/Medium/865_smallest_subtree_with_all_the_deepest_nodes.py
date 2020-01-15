# Runtime: 20 ms, faster than 80.38% of Python online submissions for Smallest Subtree with all the Deepest Nodes.
# Memory Usage: 12 MB, less than 100.00% of Python online submissions for Smallest Subtree with all the Deepest Nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, level):
        
        if root == None:
            return level
    
        dl = self.f(root.left, level+1)
        dr = self.f(root.right, level+1)
        
        # print root.val, dl, dr
        
        if dl == dr and dl >= self.max_level:
            self.ans = root
            self.max_level = dl
        
        return max(dl, dr)
    
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.max_level = -float('inf')
        self.ans = None
        
        self.f(root, 0)
        
        return self.ans