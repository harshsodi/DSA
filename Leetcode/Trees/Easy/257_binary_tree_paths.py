# Runtime: 4 ms, faster than 99.96% of Python online submissions for Binary Tree Paths.
# Memory Usage: 11.8 MB, less than 68.42% of Python online submissions for Binary Tree Paths.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def f(self, root, curr_st, str_set):
        
        if root == None:
            return str_set
    
        if root.left == None and root.right == None:
            curr_st += str(root.val)
            str_set.append(curr_st)
        
        str_set = self.f(root.left, curr_st + str(root.val) + "->", str_set)
        str_set = self.f(root.right, curr_st + str(root.val) + "->", str_set)
        
        return str_set
        
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        return self.f(root, "",[])    