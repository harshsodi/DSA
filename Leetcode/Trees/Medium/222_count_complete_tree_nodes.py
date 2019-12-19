# Runtime: 80 ms, faster than 64.93% of Python online submissions for Count Complete Tree Nodes.
# Memory Usage: 27.7 MB, less than 11.76% of Python online submissions for Count Complete Tree Nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, y):
        
        if root == None:
            return
        
        if self.caught:
            return
        
        self.max_y = max(self.max_y, y)
        
        if root.left == None and root.right == None:
            if y < self.max_y:
                self.caught = True
                return
            else:
                self.n_leaf += 1        
            
        if root.left and not self.caught:
            self.f(root.left, y+1)
        
        if root.right and not self.caught:
            self.f(root.right, y+1)
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.n_leaf = 0
        self.max_y = 0
        self.caught = False
        
        self.f(root, 0)
        
        return pow(2, self.max_y) - 1 + self.n_leaf