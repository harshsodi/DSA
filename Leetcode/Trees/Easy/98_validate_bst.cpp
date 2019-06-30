// Runtime: 20 ms, faster than 65.20% of C++ online submissions for Validate Binary Search Tree.
// Memory Usage: 20.6 MB, less than 56.86% of C++ online submissions for Validate Binary Search Tree.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    bool isValidBST(TreeNode* root) {
        
        stack<TreeNode*> st;
        st.push(root);
        
        TreeNode* prev = NULL;
        while(!st.empty()) {
            TreeNode* curr_node = st.top();
            if(curr_node == NULL) {
                st.pop();
                if(st.empty()) {
                    break;
                }
                TreeNode* par = st.top();
                st.pop();
                cout << par->val;
                if(prev && par->val <= prev->val) {
                    return false;
                }
                prev = par;
                st.push(par->right);
            } else {
                st.push(curr_node->left);
            }
        }
        
        return true;
    }
};