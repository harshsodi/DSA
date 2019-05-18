/**
 * Runtime: 16 ms, faster than 83.53% of C++ online submissions for Longest Palindromic Substring.
 * Memory Usage: 8.8 MB, less than 85.81% of C++ online submissions for Longest Palindromic Substring.
 */

class Solution {
public:

    Solution() {

    }

    string longestPalindrome(string s) {
        
        int len = s.length();
        int n = (len-1)*2;
        
        int max_len = 1;
        int initi = 0;
            
        for(int i=0 ; i<=n ; i++) {
            
            int x, y;
            
            if(i%2 == 0) {
                x = i/2;
                y = i/2;
            } else {
                x = (i-1)/2;
                y = (i+1)/2;
            }
            
            while(x >= 0 && y < len) {
                if(s[x] != s[y]) {
                    break;
                } else {
                    if(max_len < y-x+1) {
                        max_len = y-x+1;
                        initi = x;  
                    } 
                }
                
                x--;
                y++;
            }
        }
        
        return s.substr(initi, max_len);
    }
};