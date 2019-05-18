/**
 * Runtime: 8 ms, faster than 99.53% of C++ online submissions for Two Sum.
 * Memory Usage: 10.2 MB, less than 41.17% of C++ online submissions for Two Sum. 
 */


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> mp;
        vector<int> ans;

        int size = nums.size();
        for(int i=0; i<size; i++) {
            
            int complementary = target - nums[i];
            
            if(mp.find(complementary) != mp.end()) {
                ans.push_back(i);
                ans.push_back(mp[complementary]);
                break;
            } else {
                mp[nums[i]] = i;
            }
        }

        return ans;
    }
};