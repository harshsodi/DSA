# Your submission beats 24.55% Submissions!

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    
    def findClosestLeaf(self, root, k):
        # Write your code heret
    
        ans = float('inf')
        
        def find_k(root, k):
            
            if root == None:
                return None
            
            if root.val == k:
                return root
            
            l = find_k(root.left, k)
            if l:
                return l
            
            r = find_k(root.right, k)
            if r:
                return r
                
            return None
    
        def find_down(root, d, add):
            if root == None:
                return float('inf')
                
            if root.left == None and root.right == None:
                if self.maxdist > d + add:
                    self.maxdist = d + add
                    self.ans = root
                
            find_down(root.left, d+1, add)
            find_down(root.right, d+1, add)
                
        def find_par(root, k):
            if root == None:
                return float('inf')
            
            if root.val == k :
                return 0
            
            l = find_par(root.left, k)
            if l != -1:
                find_down(root.right, 1, l+1)
                return l + 1
            
            r = find_par(root.left, k)
            if r != -1:
                find_down(root.left, 1, r+1)
                return r + 1
            
            return -1
    
        self.maxdist = float('inf')
        self.ans = None
        
        kpnt = find_k(root, k)
        find_down(kpnt, 0, 0)
        
        find_par(root, k)
        
        return self.ans.val