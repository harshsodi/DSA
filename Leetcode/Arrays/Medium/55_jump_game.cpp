// Runtime: 8 ms, faster than 98.21% of C++ online submissions for Jump Game.
// Memory Usage: 9.7 MB, less than 90.43% of C++ online submissions for Jump Game.

class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        int size = nums.size();
        int curr = size - 1;
        
        for(int i = size - 1; i >=0 ; i--) {
            if (nums[i] + i >= curr) {
                curr = i;
            }
        }
        
        if(curr == 0) {
            return true;
            
        return false;
    }
};