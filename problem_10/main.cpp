
#include <iostream>
#include <vector>
#define MAX 2000000
using namespace std;

typedef long long ll;

vector<ll> getPrimes() {
    bool isPrime[MAX];

    memset(isPrime, true, sizeof(isPrime));

    for (int i = 2; i * i < MAX; ++i) {
        if (isPrime[i]) {
            // multiples of prime numbers are not prime
            for (int j = i * i; j < MAX; j += i) {
                isPrime[j] = false;
            }
        }
    }

    vector<ll> primes;

    for (int i = 2; i < MAX; ++i) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}

int main() {
    ll sum = 0;
    vector<ll> primes = getPrimes();

    for (auto i : primes)
        sum += i;

    cout << sum << endl;

    return 0;
}
