// Runtime: 12 ms, faster than 94.83% of C++ online submissions for Largest Rectangle in Histogram.
// Memory Usage: 10.6 MB, less than 31.15% of C++ online submissions for Largest Rectangle in Histogram.

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        
        int n = heights.size();
        if(n == 0) {
            return 0;
        }
        
        stack<int> s;
        long long max_area = 0;
        long long area = 0;
        
        int i;
        for(i=0; i<n; ) {
            if(s.empty() || heights[i] >= heights[s.top()]) {
                s.push(i++);             
            } else {
                int x = s.top(); s.pop();
                
                if(!s.empty()) 
                    area = heights[x] * (i-s.top()-1);
                else
                    area = heights[x] * (i);
                
                max_area = max(max_area, area);
            }
        }
        
        while(!s.empty()) {
            int x=s.top();
            s.pop();
            
            if(s.empty()) {
                area=heights[x]*i;
            } else {
                area=heights[x]*(i-s.top()-1);
            }
            max_area = max(max_area, area);
        }
        
        return max_area;
    }
};