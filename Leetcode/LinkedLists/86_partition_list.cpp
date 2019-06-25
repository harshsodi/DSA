// Runtime: 4 ms, faster than 98.66% of C++ online submissions for Partition List.
// Memory Usage: 8.8 MB, less than 13.02% of C++ online submissions for Partition List.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        
        ListNode* small = new ListNode(0);
        ListNode* smallHead = small;
        ListNode* big = new ListNode(0);
        ListNode* bigHead = big;
        
        
        while(head != NULL) {
            
            ListNode* tmp = new ListNode(head->val);
            // tmp.val = 5; //head->val;
            
            if(head->val < x) {
                small->next = tmp;
                small = small->next;
            } else {
                big->next = tmp;
                big = big->next;
            }
            
            head = head->next;
        }
        
        small->next = bigHead->next;
        return smallHead->next;
    }
};