vector<vector<int> > getMinMatrix(vector<int> arr) {
    
    // Make range minimum matrix
    int n = arr.size();
    int jSize = ceil(log2(n));

    vector<vector<int> > st(n, vector<int>(jSize));

    for(int i=0; i<n; i++) {
        st[i][0] = i;
    }

    for(int j=1; (1 << j) <= n; j++) {
        for(int i=0; (i + (1 << j)) <= n; i++) {
            if(arr[st[i][j-1]] < arr[st[i + (1 << (j-1))][j-1]]) {
                st[i][j] = st[i][j-1];
            } else {
                st[i][j] = st[i + (1 << (j-1))][j-1];
            }
        }
    }

    return st;
}

int findMin(vector<int> arr, int lo, int hi, vector<vector<int> > st) {

    int rangeSize = hi - lo + 1;
    int x=0;
    while((1<<x) <= rangeSize) {
        x++;
    }
    x--;

    int minHeightIndex;
    if(arr[st[lo][x]] < arr[st[lo + rangeSize - (1 << x)][x]]) {
        minHeightIndex = st[lo][x];
    } else {
        minHeightIndex = st[lo + rangeSize - (1 << x)][x];
    }
    
    return minHeightIndex;
}

int findLargestArea(int lo, int hi, vector<int> heights, vector<vector<int> > range_min, int& max_area) {

    if(lo > hi) {
        return max_area;
    }

    int min_height_index = findMin(heights, lo, hi, range_min);
    
    max_area = max(max_area, (hi - lo + 1) * heights[min_height_index]);

    findLargestArea(lo, min_height_index-1, heights, range_min, max_area);
    findLargestArea(min_height_index+1, hi, heights, range_min, max_area);

    return max_area;
}

class Solution {
public:
    int largestRectangleArea(vector<int> heights) {
        
        int size = heights.size();
        if(size == 0) {
            return 0;
        }
        
        if(size == 1) {
            return heights[0];
        }
        
        if(size == 2) {
            return 2*min(heights[0], heights[1]);
        }
        
        vector<vector<int> > range_min = getMinMatrix(heights);
        int max_area = 0;
        int area = findLargestArea(0, size - 1, heights, range_min, max_area);

        return area;
    }
};