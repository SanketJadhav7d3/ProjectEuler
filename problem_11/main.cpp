
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int r = 20, c = 20;
    int product = 1;  
    vector<vector<int> > grid(r, vector<int>(c, 0));

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> grid[i][j];
        }
    }

    // left right 

    for (vector<int> : i) {
        for (int j = 0; j < i.size() - 4; ++i) {
            // product of i[0] - i[4] 
            for (int a = j; a < 4; ++a) {
            }
        }
    }

    return 0;
}
