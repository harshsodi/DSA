/**
 * Runtime: 132 ms, faster than 37.24% of C++ online submissions for Longest Palindromic Substring.
 * Memory Usage: 13.1 MB, less than 48.51% of C++ online submissions for Longest Palindromic Substring.
 */

class Solution {
public:

    string longestPalindrome(string s) {
        
        if(s.length() < 2) {
            return s;
        }
        
        int n = s.length();
        int dp[n][n] = {};
        
        int max_len = 1;
        int max_i, max_j;
        
        for(int i=0; i<n; i++) {
            dp[i][i] = 1;
            max_i = i;
            max_j = i;
        }
        
        for(int i=0; i<n-1; i++) {
            if(s[i] == s[i+1]) {
                dp[i][i+1] = 1;
                max_len = 2;
                max_i = i;
                max_j = i+1;
            }
        }
        
        for(int j=0 ; j<n; j++) {
            for(int i=0; i<j; i++) {
                if(dp[i+1][j-1] == 1 && s[i] == s[j]) {
                    dp[i][j] = 1;
                    
                    if(j-i+1 > max_len) {
                        max_i = i;
                        max_j = j;
                            max_len = j-i+1;
                    }
                }
            }
        }
        
        return s.substr(max_i, max_len);
    }
};