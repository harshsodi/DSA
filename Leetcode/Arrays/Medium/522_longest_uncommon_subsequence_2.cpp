// Runtime: 4 ms, faster than 88.52% of C++ online submissions for Longest Uncommon Subsequence II.
// Memory Usage: 8.4 MB, less than 87.23% of C++ online submissions for Longest Uncommon Subsequence II.

class Solution {
public:
    
    int is_subsequence(string s1, string s2) {
         // s1 is substring of s2
        
        int p = 0;
        int len = s2.length();
        for(int i=0; i < len; i++) {
            if(s1[p] == s2[i]) {
                p++;
            }
        }
        
        return p == s1.length();
    }
    
    int findLUSlength(vector<string>& strs) {
        
        sort(strs.begin(), strs.end());
        int n = strs.size();
        
        int ans = -1;
        
        for(int i=0; i<n; i++) {
            int isans = 1;
            for(int j=0; j<n; j += 1) {
                if(i == j) continue;
                
                if(is_subsequence(strs[i], strs[j])) {
                    isans = 0;
                    break;
                }
            }
            
            if(isans == 1){ 
                int tmp = strs[i].length();
                ans = max(ans, tmp);
            }
        }
        
        return ans;
    }
};