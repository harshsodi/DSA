# Runtime: 20 ms, faster than 86.34% of Python online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.3 MB, less than 5.88% of Python online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        
        ans = []
        
        q = [root]
        
        while len(q):
            ans.append([x.val for x in q])
            next_level = []
            
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            q = next_level
        
        return ans