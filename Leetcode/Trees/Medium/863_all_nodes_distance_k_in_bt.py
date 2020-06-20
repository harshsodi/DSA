# Runtime: 28 ms, faster than 59.94% of Python online submissions for All Nodes Distance K in Binary Tree.
# Memory Usage: 13.1 MB, less than 68.13% of Python online submissions for All Nodes Distance K in Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        self.ans = []
        
        def bfs(q, lvl):
        
            if q == [None] or lvl < 0:
                return
        
            if lvl == 0:
                # print "q", q
                self.ans += [x.val for x in q]
                return
        
            if q == []:
                return
            
            next_level = []
            for ch in q:
                if ch.left != None:
                    next_level.append(ch.left)
                if ch.right != None:
                    next_level.append(ch.right)
        
            # print next_level
            bfs(next_level, lvl - 1)
        
        def f(root):
            
            if root == None:
                return None
            
            if root == target:
                bfs([root], K)
                return 0
            
            depth = 0
            
            l = f(root.left)
            if l != None:
                depth = l + 1
                if depth == K:
                    self.ans.append(root.val)
                bfs([root.right], K - depth - 1)
                return depth
        
            r = f(root.right)
            if r != None:
                depth  = r + 1
                if depth == K:
                    self.ans.append(root.val)
                bfs([root.left], K - depth - 1)
                return depth
            
            return None
    
        f(root)
        return self.ans