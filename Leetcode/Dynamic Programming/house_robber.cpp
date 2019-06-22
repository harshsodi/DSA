// Runtime: 4 ms, faster than 80.70% of C++ online submissions for House Robber.
// Memory Usage: 8.4 MB, less than 92.69% of C++ online submissions for House Robber.

class Solution {
public:
    int rob(vector<int>& nums) {
        
        int l = nums.size();
        
        if (l == 0) {
            return 0;
        } else if (l == 1) {
            return nums[0];
        } else if (l == 2) {
            return max(nums[0], nums[1]);
        }
        
        int l1 = nums[0] + nums[2];
        int l2 = nums[1];
        int l3 = nums[0];
        
        int x = l1;
        
        for(int i=3; i<l; i++) {
            
            x = nums[i] + max(l2, l3);
            
            l3 = l2;
            l2 = l1;
            l1 = x;
        }
        
        return max(x, l2);
    }
};