#include <iostream>
using namespace std;

int main() {
    int fib = 0;
    int a = 0;
    int b = 1;
    int s = 0;

    while (fib < 4000000) {
        fib = a + b;
        if (fib % 2 == 0) {
            s += fib;
        }
        a = b;
        b = fib;
    }
    cout << fib << endl;

    return 0;
}
