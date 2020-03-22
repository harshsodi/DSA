# Runtime: 16 ms, faster than 83.76% of Python online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Binary Search Tree to Greater Sum Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def f(root, sm):
            if root == None:
                return 0
            
            r_sum = f(root.right, sm)
            oval = root.val
            root.val = r_sum + sm + oval
            l_sum = f(root.left, root.val)
            
            return r_sum + l_sum + oval
    
        f(root, 0)
    
        return root