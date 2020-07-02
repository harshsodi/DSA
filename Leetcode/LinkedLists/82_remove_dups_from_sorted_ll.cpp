// Runtime: 8 ms, faster than 90.22% of C++ online submissions for Remove Duplicates from Sorted List II.
// Memory Usage: 10.9 MB, less than 71.90% of C++ online submissions for Remove Duplicates from Sorted List II.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        ListNode *h = head;
        ListNode *tmp = head;
        ListNode *useless = new ListNode(-1);
        
        while(head) {
            if(head->next && head->val == head->next->val) {
                int v = head->val;
                while(head && head->val == v) {
                    head->val = INT_MAX;
                    head = head->next;
                }
                continue;
            }
            
            head = head->next;
        }
        
        ListNode *start = new ListNode(0);
        ListNode *stmp = start;
        ListNode *runner = tmp;
        
        while(runner) {
            while(runner and runner->val == INT_MAX) {
                runner = runner->next;
            }
            start->next = runner;
            
            if(start){
                start = start->next;
            }
            
            if(runner) {
                runner = runner->next;
            }
        }
        if(start)
            start->next = runner;
        return stmp->next;
    }
};