# Runtime: 104 ms, faster than 26.80% of Python online submissions for Reorder List.
# Memory Usage: 32.4 MB, less than 11.11% of Python online submissions for Reorder List.

 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        actualHead = head
        
        if actualHead == None:
            return None
        
        if actualHead.next == None:
            return actualHead
        
        st = []
        cnt = 0
        tmp_head = actualHead
        while tmp_head:
            st.append(tmp_head)
            tmp_head = tmp_head.next
            cnt += 1
        
        ahead = actualHead
        for i in range(cnt/2):
            top = st.pop()
            sec = ahead.next
            ahead.next = top
            top.next = sec
            ahead = sec
        
        if ahead.next:
            ahead.next = None
        
        return actualHead