# Runtime: 24 ms, faster than 77.91% of Python online submissions for Split Linked List in Parts.
# Memory Usage: 12.5 MB, less than 28.57% of Python online submissions for Split Linked List in Parts.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        n = 0
        actual_root = root
        
        while root != None:
            root = root.next
            n += 1
        
        each = n/k
        rem = n%k
                
        lst = []
        for i in range(k):
            tmp = each
            if rem:
                tmp += 1
                rem -= 1
            lst.append(tmp)
            
        ans = []
        curr_head = actual_root
        curr_tail = actual_root
 
        for i in lst:
            for j in range(i-1):
                if curr_tail.next == None:
                    break
                curr_tail = curr_tail.next
            
            if curr_head and curr_tail:
                ans.append(curr_head)
                curr_head = curr_tail.next
                curr_tail.next = None
                curr_tail = curr_head
            else:
                ans.append(None)
        
        return ans