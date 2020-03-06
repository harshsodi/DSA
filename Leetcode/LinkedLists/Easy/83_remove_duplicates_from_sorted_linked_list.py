# Runtime: 28 ms, faster than 80.65% of Python online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 11.9 MB, less than 53.57% of Python online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        ahead = head

        curr = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            
            head = head.next
        
        return ahead