/**
 * Runtime: 16 ms, faster than 98.32% of C++ online submissions for Container With Most Water.
 * Memory Usage: 9.8 MB, less than 76.93% of C++ online submissions for Container With Most Water.
 */

class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int len = height.size();
        
        int i=0;
        int j=len-1;
        
        int max_area = 0;
        
        while(i<j) {
                
            max_area = max(min(height[i], height[j]) * (j-i), max_area);
            
            if(height[i] < height[j]) {
                
                int k = i+1;
                while(height[i] >= height[k] && k < j) { k++; }
                i = k;
                
            } else {
                
                int k = j-1;
                while(height[j] >= height[k] && k > i) { k--; }
                j = k;    
            }
        }
        
        return max_area;
    }
};