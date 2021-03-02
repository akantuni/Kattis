#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    while (true) {
        int n, m;
        cin >> n >> m;

        if (n == 0 and m == 0) {
            break;
        }

        unordered_set<int> s;
        int common = 0;

        for (int i = 0; i < n; i++) {
            int jack;
            cin >> jack;
            s.insert(jack);
        }

        for (int i = 0; i < m; i++) {
            int jill;
            cin >> jill;
            if (s.count(jill) > 0) {
                common++;
            }
        }
        cout << common << endl;
    }
    return 0;
}