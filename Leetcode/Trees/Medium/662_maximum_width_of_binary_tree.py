# Runtime: 28 ms, faster than 55.09% of Python online submissions for Maximum Width of Binary Tree.
# Memory Usage: 15.5 MB, less than 20.00% of Python online submissions for Maximum Width of Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 1
        self.d = {}
        
        def f(root, depth, pos):
            
            if root == None:
                return
            
            if self.d.get(depth) == None:
                self.d[depth] = pos
            
            self.ans = max(self.ans, pos - self.d[depth] + 1)
            
            f(root.left, depth+1, pos*2)
            f(root.right, depth+1, pos*2 + 1)
        
        f(root, 0, 0)
        return self.ans