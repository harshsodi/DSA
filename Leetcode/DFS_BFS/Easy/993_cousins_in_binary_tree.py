# Runtime: 20 ms, faster than 68.75% of Python online submissions for Cousins in Binary Tree.
# Memory Usage: 12.8 MB, less than 8.33% of Python online submissions for Cousins in Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        self.xans = None
        self.yans = None
        
        def f(rt, level, parent):
            if rt == None:
                return
            
            if rt.val == x:
                if self.yans != None:
                    return (level == self.yans[0] and parent != self.yans[1])
                    # print self.yans, level, parent
                else:
                    self.xans = [level, parent]
            
            if rt.val == y:
                if self.xans != None:
                    # print self.xans, level, parent
                    return (level == self.xans[0] and parent != self.xans[1])
                else:
                    self.yans = [level, parent]
        
            return f(rt.left, level+1, rt.val) or f(rt.right, level+1, rt.val)
        
        fans = f(root, 0, None)
        # print fans
        return fans