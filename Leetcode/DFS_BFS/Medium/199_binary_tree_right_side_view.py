# Runtime: 20 ms, faster than 64.05% of Python online submissions for Binary Tree Right Side View.
# Memory Usage: 11.8 MB, less than 39.29% of Python online submissions for Binary Tree Right Side View.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        
        ans = []
        q = [root]
        
        while len(q):
            
            last = q[-1]
            ans.append(last.val)
            
            next_level = []
            
            for i in range(len(q)):
                top = q.pop(0)
                
                if top.left != None:
                    next_level.append(top.left)
                
                if top.right != None:
                    next_level.append(top.right)
                            
            q = next_level
        
        return ans
                