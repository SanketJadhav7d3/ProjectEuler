
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> generate_primes(int n) {
    bool is_primes[n];

    // fill all the values with 0
    memset(is_primes, true, sizeof(is_primes));

    for (int i = 2; i*i < n; ++i) {
        if (is_primes[i]) {
            for (int j = i*i; j < n; j += i) {
                is_primes[j] = false;
            }
        }
    }

    vector<int> primes;

    for (int i = 2; i < n; ++i) {
        if (is_primes[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}

bool is_pandigital(int n) {
    vector<int> a;
    vector<int> digits;
    int rem;

    int digit_count = int(log10(n) + 1);

    for (int i = 1; i <= digit_count; ++i) 
        a.push_back(i);

    while (n > 0) {
        rem = n % 10;
        digits.push_back(rem);
        n /= 10;
    }

    sort(digits.begin(), digits.end());

    if (digits == a) 
        return true;

    return false;
}

int main() {
    vector<int> a;

    a = generate_primes(8000000);

    for (int i : a) {
        if (is_pandigital(i))
            cout << i << endl;
    }
    return 0;
}
