class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        
        int len = nums.size();
        
        if(!len) 
            return 0;
        
        int ans = len + 1;
        int sums[len];
        
        sums[0] = nums[0];
        
        for(int i=1; i<len; i++)
            sums[i] = sums[i-1] + nums[i];
        
        for(int i=0; i<len; i++) {
            for(int j=i; j<len; j++) {
                int x = sums[j] - sums[i] + nums[i];
                if(x >= s) {
                    ans = min(ans, j-i+1);
                    break;
                }
            }
        }
        
        if(ans > len) {
            return 0;
        } else {
            return ans;
        }
        
    }
};