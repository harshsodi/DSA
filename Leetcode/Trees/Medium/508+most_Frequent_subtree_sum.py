# Runtime: 44 ms, faster than 53.40% of Python online submissions for Most Frequent Subtree Sum.
# Memory Usage: 19.6 MB, less than 25.00% of Python online submissions for Most Frequent Subtree Sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        self.d = {}
        
        def f(root):
            
            if root == None:
                return 0
            
            sm = root.val + f(root.left) + f(root.right)
            self.d[sm] = self.d.get(sm, 0) + 1
            return sm
    
        f(root)
    
        seq = list(sorted([(i, self.d[i]) for i in self.d], key=lambda x: x[1], reverse=True))
        print seq
        
        curr = seq[0][1]
        ans = []
        
        for i in seq:
            if i[1] != curr:
                break
            
            ans.append(i[0])
            curr = i[1]
        
        return ans