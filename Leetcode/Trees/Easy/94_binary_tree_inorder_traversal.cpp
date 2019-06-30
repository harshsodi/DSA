// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Inorder Traversal.
// Memory Usage: 9.5 MB, less than 13.26% of C++ online submissions for Binary Tree Inorder Traversal.

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
    
    void trav(TreeNode* root, vector<int>& ans) {
        
        if(root) {
            trav(root->left, ans);
            cout << root->val << endl;
            ans.push_back(root->val);
            trav(root->right, ans);
        }   
    }
    
    vector<int> inorderTraversal(TreeNode* root) {
        
        vector<int> x;
        trav(root, x);
        return x;
    }
};