#include <iostream>
using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {
        int l, r, u, d;
        int x,y, x1, y1, x2, y2;

        cin >> l >> r >> d >> u;
        cin >> x >> y >> x1 >> y1 >> x2 >> y2;

        int ans = 1;

        // Handle horizontal movement
        if(r > l) {
            // Move as left as possible
            int shift = max(x1, x-l);
            l -= abs(x-shift);

            cout << "Moved left to " << shift << endl;
            cout << "L " << l << " -- R " << r << endl;

            if((r-l) > (x2 - shift)) {
                ans = 0;
            }

        } else {
            // Move as right as possible
            int shift = min(x2, x+r);
            r -= abs(shift - x);

            cout << "Moved right to " << shift << endl;
            cout << "L " << l << " -- R " << r << endl;

            if((l-r) > (shift - x1)) {
                ans = 0;
            }
        }

        // Handle vertical movement
        if(u > d) {
            // Move as left as possible
            int shift = max(y1, y-d);
            d -= abs(y-shift);

            cout << "Moved down to " << shift << endl;
            cout << "D " << d << " -- U " << u << endl;

            if((u-d) > (y2 - shift)) {
                ans = 0;
            }

        } else {
            // Move as right as possible
            int shift = min(y2, y+u);
            u -= abs(shift - y);

            cout << "Moved up to " << shift << endl;
            cout << "D " << d << " -- U " << u << endl;

            if((d-u) > (shift - y1)) {
                ans = 0;
            }
        }

        if(ans == 1) {
            cout << "Yes\n" << endl;
        } else {
            cout << "No\n" << endl;
        }

    }
}