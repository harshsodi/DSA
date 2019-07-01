# Runtime: 16 ms, faster than 98.94% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 11.8 MB, less than 49.24% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def create(self, value, root):
        
        if root == None:
            root = TreeNode(value)
        else:
            if value < root.val:
                if not root.left:
                    root.left = TreeNode(value)
                else:
                    self.create(value, root.left)
            else:
                if not root.right:
                    root.right = TreeNode(value)
                else:
                    self.create(value, root.right) 
    
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        self.root = None
        for i in preorder:
            if not self.root:
                self.root = TreeNode(i)
            else:
                self.create(i, self.root)
        
        return self.root