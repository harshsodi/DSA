# Runtime: 388 ms, faster than 55.65% of Python online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 17.9 MB, less than 100.00% of Python online submissions for All Elements in Two Binary Search Trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        
        res = []
        
        def f(root, st):
            if root == None:
                return
            st.append(root)
            f(root.left, st)
        
        st1 = []
        st2 = []
        
        f(root1, st1)
        f(root2, st2)
        
        while len(st1) and len(st2):
            r1 = st1[-1]
            r2 = st2[-1]
            
            if r1.val < r2.val:
                res.append(r1.val)
                st1.pop()
                f(r1.right, st1)
            else:
                res.append(r2.val)
                st2.pop()
                f(r2.right, st2)
        
        s = st1
        if len(st1) == 0:
            s = st2
        
        while len(s):
            top = s.pop()
            res.append(top.val)
            f(top.right, s)
        
        return res