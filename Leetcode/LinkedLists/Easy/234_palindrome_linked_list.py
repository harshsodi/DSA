# Runtime: 60 ms, faster than 94.20% of Python online submissions for Palindrome Linked List.
# Memory Usage: 31.1 MB, less than 10.34% of Python online submissions for Palindrome Linked List.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #find len
        head_c = head
        
        l = 0
        while head_c:
            l += 1
            head_c = head_c.next
        
        
        if l < 2:
            return True
        
        head_c = head
        for i in range(l/2):
            head_c = head_c.next
        
        prev = None
        temp = head_c.next
        while temp:
            temp = head_c.next
            head_c.next = prev
            prev = head_c
            
            if temp != None:
                head_c = temp
        
        while head_c:
            if head_c.val != head.val:
                return False
            head_c = head_c.next
            head = head.next
        
        return True