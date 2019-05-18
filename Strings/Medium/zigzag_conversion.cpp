/**
 * Runtime: 4 ms, faster than 99.95% of C++ online submissions for ZigZag Conversion.
 * Memory Usage: 14.6 MB, less than 62.65% of C++ online submissions for ZigZag Conversion.
 */

class Solution {
public:

    Solution() {

    }

    string convert(string s, int numRows) {
        
        if(numRows == 1 || numRows == s.length()) {
            return s;
        }

        int n = s.length();
        vector<string> rows(n, "");
  
        int change = 1;
        int row = 0;
        
        for(int i=0; i<n; i++) {
            
            // cout << "Row " << row << endl; 

            rows[row] += s[i];
            
            if(row == 0) { change = 1; }
            if(row == numRows-1) { change = -1; }

            row += change;
        }
        
        string ans = "";
        // cout << "rows :" << rows[1] << endl;
        for(int i=0 ; i<n ; i++) {
            ans.append(rows[i]);
        }
        
        return ans;
    }
};