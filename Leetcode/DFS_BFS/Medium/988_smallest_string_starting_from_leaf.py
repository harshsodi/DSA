# Runtime: 36 ms, faster than 83.66% of Python online submissions for Smallest String Starting From Leaf.
# Memory Usage: 15.9 MB, less than 100.00% of Python online submissions for Smallest String Starting From Leaf..

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        
        self.strs = []
        self.add = ord('a')
        
        def f(root, st):
            
            curch = chr(self.add + root.val)
            curst = curch + st
            
            if root.left == None and root.right == None:
                self.strs.append(curst)
            
            if root.left:
                f(root.left, curst)
            
            if root.right:
                f(root.right, curst)
            
        f(root, "")
        return min(self.strs)