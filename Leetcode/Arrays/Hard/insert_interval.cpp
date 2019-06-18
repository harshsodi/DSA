// Runtime: 16 ms, faster than 80.43% of C++ online submissions for Insert Interval.
// Memory Usage: 12.6 MB, less than 7.72% of C++ online submissions for Insert Interval.

bool sortByStart(vector<int> v1, vector<int> v2) {
    return v1[0] < v2[0];
}


class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
        if(intervals.size() == 0) {
            intervals.push_back(newInterval);
            return intervals;
        }
        
        vector<vector<int>>::iterator it = intervals.begin();
        int len = intervals.size();
        int i;
        int flag = 0;
        
        for(i=0; i<len; i++) {
            if(intervals[i][0] >= newInterval[0]) {
                intervals.insert(it, newInterval);
                flag = 1;
                break;
            }   
            it = next(it,1);
        }
        
        if(!flag)
            intervals.push_back(newInterval);
           
        vector<vector<int>> new_list {intervals[0]};
        int l = 0;
        
        for(int i=1; i<=len; i++) {
            if(new_list[l][1] < intervals[i][0]) {
                new_list.push_back(intervals[i]);
                l += 1;
            } else {
                new_list[l][1] = max(intervals[i][1], new_list[l][1]);
            }
        }
        
        return new_list;
    }
};