
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <thread>
using namespace std;

int getTriangleNumber(int i) {
    return (i * (i + 1)) / 2;
}

int getDivisorCount(int n) {
    int count = 0;
    for (int i = 1; i <= n; ++i) {
        if (n % i == 0) {
            count++; 
        }
    }
    return count;
}

void getDivisors(int n) {
    vector<int> divisors;
    for (int i = 1; i <= n; ++i) {
        if (n % i == 0) {
            divisors.push_back(i);
        }
    }

    for (int i : divisors) {
        cout << i << " ";
    }

    cout << endl;
}

int main() {
    int t; 
    int count;

    for (int i = 0; i < 13000; ++i) {
        t = getTriangleNumber(i);
        count = getDivisorCount(t);

        cout << count << endl;
        if (count > 500) {
            cout << "Answer: " << count << endl;
            break;
        }
    }
    return 0;
}
