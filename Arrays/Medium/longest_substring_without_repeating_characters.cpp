/**
 * Runtime: 8 ms, faster than 99.62% of C++ online submissions for 
 * Longest Substring Without Repeating Characters.
 * 
 * Memory Usage: 10 MB, 
 * less than 86.30% of C++ online submissions for 
 * Longest Substring Without Repeating Characters.
 */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_map<char, int> mp;

        vector<int> m(128, -1);

        int n = s.length();
        int max_string = 0;
        
        for(int i=0, j=0; j < n; j++) {
            
            char ch = (int)s[j];
            if(m[ch] != -1) {
                i = max(i, m[ch]+1);
            }

            max_string = max(max_string, j-i+1);
            m[ch] = j;
        }
        
        return max_string;
    }
};