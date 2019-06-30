# Runtime: 44 ms, faster than 94.61% of Python online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 19.4 MB, less than 96.14% of Python online submissions for Find Mode in Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        curr = root
        st = []

        curr_num = None
        max_count = 0
        curr_count = 0
        ans = []
        
        while True:
            if curr == None:
                if not st:
                    break
                else: 
                    curr = st.pop()
                    
                    if curr_num == None:
                        curr_num = curr.val
                    if curr_num == curr.val:
                        curr_count += 1
                    else:
                        curr_num = curr.val
                        max_count = max(curr_count, max_count)
                        curr_count = 1
                        
                    if curr_count == max_count:
                        ans.append(curr_num)
                    if curr_count > max_count:
                        ans = [curr_num]
                        
                    # print "Cons: ", curr.val, "CurNum: ", curr_num, "CurCnt: ", curr_count, "Max: ", max_count, ans
                    
                    curr = curr.right
            else:
                st.append(curr)
                curr = curr.left
            
        print max_count, ans
        return ans