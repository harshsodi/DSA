# Runtime: 84 ms, faster than 94.21% of Python online submissions for Deepest Leaves Sum.
# Memory Usage: 20.3 MB, less than 100.00% of Python online submissions for Deepest Leaves Sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ans = None
        q = [root]
        
        while len(q):
            sm = 0
            next_level = []
            
            for node in q:
                sm += node.val
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            ans = sm
            
            q = next_level
        
        return ans