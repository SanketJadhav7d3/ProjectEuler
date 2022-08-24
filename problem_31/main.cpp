
#include <iostream>
using namespace std;

int main() {
    long long int target = 200;
    long long int coins[] = {1, 2, 5, 10, 20, 50, 100, 200};
    long long int coins_size = sizeof(coins) / sizeof(coins[0]);
    long long int tables[target + 1];
    tables[0] = 1;

    for (long long int i = 0; i < coins_size; i++) {
        for (long long int j = coins[i]; j <= target; j++) {
            tables[j] += tables[j - coins[i]];
        }
    }

    for (long long int i = 0; i < 201; ++i) {
        cout << tables[i] << endl;
    }

    return 0;
}
