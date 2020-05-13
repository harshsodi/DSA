# Runtime: 56 ms, faster than 31.40% of Python online submissions for Unique Binary Search Trees II.
# Memory Usage: 16.7 MB, less than 12.50% of Python online submissions for Unique Binary Search Trees II.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def f(lbound, rbound):
            
            if lbound > rbound:
                return [None]
            
            if lbound == rbound:
                return [TreeNode(lbound)]
        
            tans = []
        
            for curr_val in range(lbound, rbound+1):
                for l in f(lbound, curr_val-1):
                    for r in f(curr_val+1, rbound):
                        newnode = TreeNode(curr_val)
                        newnode.left = l
                        newnode.right = r
                        
                        tans.append(newnode)
            
            return tans
        
        ans = f(1, n)
        if ans[0] == None:
            return []
        return ans