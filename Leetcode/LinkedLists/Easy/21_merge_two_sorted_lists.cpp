// Runtime: 4 ms, faster than 98.93% of C++ online submissions for Merge Two Sorted Lists.
// Memory Usage: 9 MB, less than 66.39% of C++ online submissions for Merge Two Sorted Lists.

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        if(l1 == NULL) {
            return l2;
        }
        
        if(l2 == NULL) {
            return l1;
        }
        
        ListNode *l1h = l1;
        ListNode *l2h = l2;
        
        ListNode *final_head = NULL;
        
        while(l1 != NULL && l2 != NULL) {
            
            if(l1->val <= l2->val) {
            
                if(final_head == NULL)
                    final_head = l1;
                
                while(l1->next != NULL && l1->next->val <= l2->val)
                    l1 = l1->next;
                
                ListNode *temp = l1->next;
                l1->next = l2;
                
                l1 = temp;
            
            } else {
            
                if(final_head == NULL)
                    final_head = l2;
                
                while(l2->next != NULL && l2->next->val <= l1->val)
                    l2 = l2->next;
                
                ListNode *temp = l2->next;
                l2->next = l1;
                                
                l2 = temp;
            }
        }
        
        return final_head;
    }
};