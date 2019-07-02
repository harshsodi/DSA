#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n;
    cin >> n;

    string s;
    cin >> s;

    vector<int> pre[26];
    for(int i=0; i<n; i++) {
        pre[s[i] - 'a'].push_back(i);
    }

    int m;
    cin >> m;

    for(int i=0; i<m; i++) {
        string q;
        cin >> q;

        int q_len = q.length();
        int max_cnt = 0;
        map<int, int> um;
        
        for(int j=0; j<q_len; j++) {
            if(um.find(q[j]) != um.end()) {
                um[q[j]] += 1;
            } else {
                um[q[j]] = 0;
            }

            max_cnt = max(max_cnt, pre[q[j] - 'a'][um[q[j]]]);
        }

        cout << max_cnt + 1 << endl;
    }
}