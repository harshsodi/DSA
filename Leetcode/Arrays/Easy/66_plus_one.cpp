// Runtime: 4 ms, faster than 83.81% of C++ online submissions for Plus One.
// Memory Usage: 8.5 MB, less than 77.32% of C++ online submissions for Plus One.

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        int size = digits.size();
        int carry = 1;
        
        for(int i=size-1; i>=0; i--) {
            
            int curr = digits[i] + carry;
            
            if(curr >= 10) {
                carry = 1;
                curr -= 10;
            } else {
                carry = 0;
            }
            
            digits[i] = curr;
        }

        if(carry) {
            digits.insert(digits.begin(),1);   
        }
        
        return digits;
        
    }
};