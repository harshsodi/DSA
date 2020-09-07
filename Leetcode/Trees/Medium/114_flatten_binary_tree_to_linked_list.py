# Runtime: 32 ms, faster than 45.49% of Python online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 13.5 MB, less than 96.85% of Python online submissions for Flatten Binary Tree to Linked List.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def f(root, tail):
            
            if root == None:
                return
            
            if root.left == None:
                f(root.right, None) # Flatten the right side and return root
            else:
                new_tail = root.right
                root.right = f(root.left, new_tail)
                root.left = None
            
            x = root
            while x.right != None:
                x = x.right
            x.right = f(tail, None)
            
            return root
        
        f(root, None)