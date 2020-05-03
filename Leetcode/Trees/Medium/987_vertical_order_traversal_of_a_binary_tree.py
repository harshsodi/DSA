# Runtime: 20 ms, faster than 82.28% of Python online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 13.1 MB, less than 25.00% of Python online submissions for Vertical Order Traversal of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        mp = {}
        
        def f(root, x, y):
            
            if root == None:
                return
            
            if mp.get(x) == None:
                mp[x] = {}
            
            if mp[x].get(y) == None:
                mp[x][y] = []
            
            mp[x][y].append(root.val)
            
            f(root.left, x-1, y+1)
            f(root.right, x+1, y+1)
            
        ans = []
        f(root, 0, 0)
        
        for xs in sorted(mp.keys()):
            tans = []
            for ys in sorted(mp[xs].keys()):
                tans = tans + sorted(mp[xs][ys])
            
            ans.append(tans)
        return ans