/**
 * Runtime: 2 ms, faster than 95.00% of Java online submissions for Add Two Numbers.
 * Memory Usage: 43.5 MB, less than 87.41% of Java online submissions for Add Two Numbers.
 */

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* l3 = new ListNode(0);
        ListNode* head;
        
        head = l3;
        
        int curr_sum;
        int carry = 0;
        
        while(l1 || l2) {
            
            curr_sum = 0;
            if(l1) { curr_sum += l1->val; }
            if(l2) { curr_sum += l2->val; }
            
            curr_sum += carry;
            carry = (curr_sum >= 10) ? 1 : 0;
            
            ListNode* temp = new ListNode(curr_sum % 10);
            l3->next = temp;
            l3 = l3->next;

            l1 = (l1 && l1->next) ? l1->next : NULL;
            l2 = (l2 && l2->next) ? l2->next : NULL;
        }
        
        if(carry) {
            l3->next = new ListNode(1);
        }
        
        return head->next;
    }
};